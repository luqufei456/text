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

#根据用户名查询密码
sql = 'select passwd from users wehre name =%s'
helper = MysqlHelper('localhost', 3306, 'python3', 'root', 'woaiex008')
result = helper.all(sql, [name])
#(('woaiex008',),)

#验证
if len(result) == 0:
    print("用户名错误")
elif result[0][0] == passwd2:
    print('登录成功')
else:
    print("密码错误")