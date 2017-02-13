# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    server tool be used to received gps data, analyse gps data
    and import to mysql database,
    database is only support mysql
    and can expand database in dbhandler file according to demand

demo:

if __name__ == "__main__":
    host = ""
    port = 1990
    addr = (host, port)
    print "Server start"
    server = SocketServer.ThreadingTCPServer(addr, TCPRequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()
------------------------------------------------
"""
import threading
import binascii
from SocketServer import BaseRequestHandler
from datetime import datetime

from config import *
from dbhandler import *
from log import *

SOCKET_DATA_MAX = 1024
FORMMAT = "%Y-%m-%d %H:%M:%S"


class TCPRequestHandler(BaseRequestHandler):
    """
    The RequestHandler class for my server.
    It is instantiated once per connection to the server, and must
    override the handle method to implement communication to the
    client.
    """

    def setup(self):
        BaseRequestHandler.setup(self)

    def handle(self):
        host, port, user, password, database = get_db_config()
        gps_table = get_gps_table_config()
        try:
            dbhandle = DBHandler(host=host,
                                 port=port,
                                 user=user,
                                 password=password,
                                 database=database)
            dbhandle.open()
            log.info("TCPRequestHandler handle dbhandler is open")
        except Exception as e:
            emsg = "TCPRequestHandler handle dbhandler open is error: %s" % e.message
            log.error(emsg)
        client = self.client_address
        cur_thread = threading.current_thread().name
        log.info("gps server %s receive %s data" % (cur_thread, client))
        while True:
            try:
                gps_data_2 = self.request.recv(SOCKET_DATA_MAX).strip()
                if gps_data_2:
                    try:
                        cur_time = datetime.now()
                        gps_data_16 = binascii.b2a_hex(gps_data_2)
                        value = str(TCPRequestHandler.gps_parse(gps_data_16, cur_time))
                        insert_values = "insert into %s values %s ;" % (gps_table, value)
                        dbhandle.insert(insert_values)
                    except Exception as e:
                        emsg = "TCPRequestHandler dbhandle gps is error: %s" % e.message
                        log.error(emsg)
            except Exception as e:
                # emsg = "%s is break off gps server: %s" % (client, e.message)
                # log.error(emsg)
                # break
                continue
        dbhandle.close()

    @staticmethod
    def gps_parse(data, cur_time):
        assert isinstance(data, basestring)
        dataTime = ''
        terminalId = data[10:22]
        state = bin(int(data[34:42], 16))
        lat = int(data[42:50], 16) * 0.0001 / 60
        lon = int(data[50:58], 16) * 0.0001 / 60
        speed = int(data[58:62], 16) * 0.1
        direct = int(data[62:64], 16)
        time = bin(int(data[64:76], 16))
        state = state[2:]
        time = time[2:]
        stateAddZero = 32 - len(state)
        timeAddZero = 48 - len(time)
        for j in range(stateAddZero):
            state = '0' + state
        for k in range(timeAddZero):
            time = '0' + time
        for i in range(0, 48, 4):
            dataTime += str(int(time[i:i + 4], 2))
        state = state[3]
        gps_time = datetime.strptime(dataTime, '%y%m%d%H%M%S')
        delays = (cur_time - gps_time).seconds
        return terminalId, str(gps_time), lon, lat, speed, direct, state, delays
