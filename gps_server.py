# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    gps_server be used to receive, analyse, import database about gps source
    it need run to modify config file that contains server host, server port,
    database host, database port, database user, database password, database default

        +------------+
        | Run Server |
        +------------+
              |
              v
        +------------+
        | Recive GPS | --<--
        +------------+      ^
              |             |
              v             |
        +------------+      ^
        |Analyse GPS |      |
        +------------+      |
              |             ^
              v             |
        +------------+      |
        | Import GPS | -->--
        +------------+

------------------------------------------------
"""
import SocketServer

from core.config import *
from core.server import *


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/7"


if __name__ == "__main__":
    host, port = get_server_config()
    addr = (host, port)
    msg = "GPS Server %s start run......" % str(addr)
    log.info(msg)
    server = SocketServer.ThreadingTCPServer(addr, TCPRequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()
