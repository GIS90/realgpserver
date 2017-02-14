# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
from SocketDemo.ZhiShuSys_GPS_Server_15S.core.dbhandler import *

host = "localhost"
port = 3306
user = "root"
password = "123456"
database = "test"

dbhandle = DBHandler(host=host,
                     port=port,
                     user=user,
                     password=password,
                     database=database)
conn = dbhandle.open()
query_sql = "select * from gps limit 10"
rlt = dbhandle.query(query_sql, 2)
insert_sql = "insert into link values(100, 550, 100, 100, 100, 100), (111, 550, 11, 11, 111, 111);"
dbhandle.insert(insert_sql)
dbhandle.close()



