#1.打印功能提示
print("="*50)
print("    名字管理系统")
print("1:添加一个新名字")
print("2:删除一个名字")
print("3:修改一个名字")
print("4:查询一个名字")
print("5.退出系统")
print("="*50)
names = []  # 定义一个空的列表用于添加名字
while True:#当不知道程序该运行多少次时，True让程序一直循环运行，除非被break结束
#2.获取用户选择
    num = int(input("请输入功能序号(1-5)："))

#3.根据用户选择执行相应功能
    if num == 1:
        name1 = input("请输入名字：")
        names.append(name1)
        print(names)
    elif num == 2:
        del_name = input("请输入想要删除的名字：")
        if del_name in names:
            names.remove(del_name)
            print(names)
        else:
            print("无法删除，要删除的名字不存在")
    elif num == 3:
        edit_name = input("请输入想要修改的名字：")
        if edit_name in names:
            edit_name1 = input("请输入新名字：")
            a = int(names.index(edit_name))#查找该名字的下标
            names[a] = edit_name1#利用下标修改名字
        else:
            print("无法修改，需要修改的名字不存在")
    elif num == 4:
        find_name = input("请输入想要查询的名字：")
        if find_name in names:
            print("查询到该名字")
        else:
            print("没找到该名字")
    elif num == 5:
        break
    else:
        print("请输入正确的功能序号")