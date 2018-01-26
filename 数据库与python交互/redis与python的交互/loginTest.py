#coding=utf-8
from redisTest import redisHelper
from MysqlHelper import MysqlHelper
from hashlib import sha1

#接收输入
name = input("请输入用户名：")
pwd1 = input("请输入密码：")

#加密
s1 = sha1()
s1.update(pwd1)
pwd2 = s1.hexdigest()

#查询redis中是否存在此用户
r = redisHelper("localhost", 6379)
m = MysqlHelper("localhost", 3306, "python3", "root", "woaiex008")
#判断redis中是否存储了用户名和密码
if r.get(name) == None:
    sql = "select passwd from users where name=%s"
    pwd3 = m.one(sql, [name])
    if pwd3 ==None:
        print("用户名错误")
    else:
        r.set(name, pwd3[0])
        if pwd3[0] == pwd2:
            print("登录成功")
        else:
            print("密码错误")
#根据用户名，在mysql中查询，如果查询了数据，则在redis中存储
else:
    if r.get(name) == pwd2:
        print("登录成功")
    else:
        print("密码错误")