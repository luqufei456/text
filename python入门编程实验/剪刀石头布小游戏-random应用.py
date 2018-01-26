import random #导入随机取数模块

#提示并获取用户的输入
player = int(input("请输入你的选择：石头(0) 剪刀(1) 布(2) "))#保存玩家的输入选择

#让电脑自动出一个
computer = random.randint(0,2)#0-2中随机取整数值

#判断用户的输入，并显示对应的结果
if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==0):#玩家获胜的条件
    print("恭喜~获取胜利")
elif player==computer:#玩家平局的条件
    print("平局了，再来一局吧")
else: #输掉的条件
    print("你输了，再来一局吧")