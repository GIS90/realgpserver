# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
from SocketDemo.ZhiShuSys_GPS_Server_15S.core.command import *

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/11"

command = "netstat -ano | findstr 80"
retcode = COMMAND.execute(command, is_repipe=False)
print retcode






