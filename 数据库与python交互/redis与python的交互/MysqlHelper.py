# 封装之后作为一个包
# coding=utf-8
from MySQLdb import *


class MysqlHelper(object):
    def __init__(self, host, port, db, user, passwd, charset='uft8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,
                            charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def cub(self, sql, params):
        try:
            self.open()

            self.cursor.execute(sql, params)
            self.conn.commit()

            self.close()

        except Exception as e:
            print(e)

    def all(self, sql, params=[]):  # 查询不需要params，这里默认空列表
        try:
            self.open()

            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()

            self.close()

            return result
        except Exception as e:
            print(e)

    def one(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
            return result

        except Exception as e:
            print(e)