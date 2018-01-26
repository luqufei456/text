#coding=utf-8
from MysqlHelper import MysqlHelper
from hashlib import sha1

#接收用户输入
name = input("请输入用户名：")
passwd = input("请输入密码：")

#对密码加密
s1 = sha1()
s1.update(passwd)
passwd2 = s1.hexdigest()

#查询用户名是否存在
sql = 'select * from users wehre name =%s'
helper = MysqlHelper('localhost', 3306, 'python3', 'root', 'woaiex008')
result = helper.all(sql, [name])

sql1 = 'insert into users values(0,%s,%s)'
#验证
if len(result) == 0:
    print("用户名可用")
    helper.cub(sql1, [name, passwd2])
    print("注册成功")
else:
    print("用户名已存在，请重新输入")