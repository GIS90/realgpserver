# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
------------------------------------------------
"""

import time
from socket import *

host = '192.168.2.108'
port = 1990
bufsize = 1024
addr = (host, port)
client = socket(AF_INET, SOCK_STREAM)
client.connect(addr)
while True:
    # for i in range(1, 5):
    data = ""
    for j in range(1, 20000):
        rlt = data + "7e0200001c101004332812000200008000000081010000000000000000000000160503175909f00100b77e,"
        data = rlt
    client.sendall(data[:-1])
    print "client send data to server"
    time.sleep(5)
    # break
client.close()
