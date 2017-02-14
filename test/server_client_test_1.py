# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

import time
from socket import *

host = '127.0.0.1'
port = 5432
bufsize = 1024
addr = (host, port)
client = socket(AF_INET, SOCK_STREAM)
client.connect(addr)
data = "7e0200001c101004332812000200008000000081010000000000000000000000160503175909f00100b77e\n"
while True:
    print data
    client.sendall(data)
client.close()
