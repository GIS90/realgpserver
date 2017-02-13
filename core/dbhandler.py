# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    Mysql database interface that to operate msyql
    method contains open, close, insert, query and pivate __open
    database is only support mysql

demo:
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
------------------------------------------------
"""
import mysql.connector

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/7"
__dbhandler_method__ = ["open", "close", "query", "insert"]


# operate mysql class
class DBHandler:
    def __init__(self, host, port, user, password, database):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database
        self.__conn = None

    def open(self):
        """
        open mysql connection
        :return: mysql connect object
        if failure reture None
        """
        try:
            return self.__open()
        except Exception as e:
            emsg = "DBHandler open is error: %s" % e.message
            raise Exception(emsg)

    def __open(self):
        self.conn = mysql.connector.connect(host=self.__host,
                                            port=self.__port,
                                            user=self.__user,
                                            passwd=self.__password,
                                            db=self.__database)

        return self.conn

    def close(self):
        """
        close mysql database connection if connection is not None
        :return: True
        such as:
            dbhandle.close()
        """
        try:
            if self.conn is not None:
                self.conn.close()
            return True
        except Exception as e:
            emsg = "DBHandler close is error: %s" % e.message
            raise Exception(emsg)

    def query(self, sql, ret_type, times=5):
        """
        :param sql: execute query sql
        :param ret_type: return result type
        :param times: query times, default is 5
        :return: if ret_type is 1, return result is string value
                 if ret_type is 2, return result is list value
        such as:
            sql = "select * from gps limit 10"
            ret_type = 2
            or
            sql = "select count(*) from gps"
            ret_type = 1

            rlt = dbhandle.query(sql, 2)
        """
        assert isinstance(sql, basestring)
        assert isinstance(ret_type, int)
        assert ret_type in range(1, 3)
        if self.conn is None:
            for i in range(1, times, 1):
                if self.open():
                    break
                if i == times:
                    emsg = "'DBHandler query open mysql failure"
                    raise Exception(emsg)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            ret_values = cursor.fetchall()
            if not ret_values:
                return "0" if 1 == ret_type else []
            if ret_type == 1:
                return str(ret_values[0][0])
            elif ret_type == 2:
                return list(ret_values)
        except Exception as e:
            emsg = 'DBHandler query is exception: %s' % e.message
            raise Exception(emsg)

    def insert(self, insert_sql, times=5):
        assert isinstance(insert_sql, basestring)
        if self.conn is None:
            for i in range(1, times, 1):
                if self.open():
                    break
                if i == times:
                    emsg = "'DBHandler insert open mysql failure"
                    raise Exception(emsg)
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            emsg = 'DBHandler insert is exception: %s' % e.message
            raise Exception(emsg)
