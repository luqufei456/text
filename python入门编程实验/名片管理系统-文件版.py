card_infors = []#定义一个空列表用来存储名片

def print_menu():
    """完成打印功能菜单"""   #函数文档的说明
    print("="*50)
    print("名片管理系统")
    print("1.添加一个新名片")
    print("2.删除一个名片")
    print("3.修改一个名片")
    print("4.查询一个名片")
    print("5.显示所有的名片")
    print("6.保存信息")
    print("7.退出系统")
    print("="*50)

def add_new_card_infor():
    """完成添加一个新的名片"""
    new_name = input("请输入新的名字：")
    new_qq = input("请输入新的QQ：")
    new_high = input("请输入新的身高：")
    new_addr = input("请输入新的住址：")
    new_telephon = input("请输入新的电话号码：")

    # 定义一个新的字典用来存储名片
    new_infor = {}
    new_infor["name"] = new_name
    new_infor["qq"] = new_qq
    new_infor["high"] = new_high
    new_infor["addr"] = new_addr
    new_infor["telephon"] = new_telephon

    #global card_infors   因为最开始定义了一个全局变量 所以可以直接使用
    card_infors.append(new_infor)  # 将新名片导入列表中
    # print(card_infors) #for test

def dele_name():
    """删除输入的名片"""
    # global card_infors    一般在函数最开始声明比较好
    dele_name = input("请输入想要删除的名片")
    find_flag1 = 0  # 默认表示没有找到
    for name_ in card_infors:
        if dele_name == name_["name"]:
            card_infors.remove(name_)
            print("已删除")
            find_flag1 = 1
            break
    if find_flag1 == 0:
        print("没有你要删除的名片")

def modify_name_card():
    """修改输入的名片"""
    # global card_infors
    modify_name = input("请输入想要修改的名片姓名")
    find_flag2 = 0  # 默认表示没有找到
    modify_flag = 0  # 默认表示没有修改成功
    sign = 0
    for name_a in card_infors:  # 在列表里一个个查找字典 查找一次循环一次
        sign += 1
        if modify_name == name_a["name"]:
            find_flag2 = 1
            print("1.修改姓名")  # 打印菜单
            print("2.修改QQ")
            print("3.修改身高")
            print("4.修改住址")
            print("5.修改电话号码")
            print("6.退出修改系统")
            while True:
                num1 = int(input("请输入你要修改信息的编号"))  # 输入修改项对应的编号
                if num1 == 1:
                    card_infors[sign - 1]["name"] = input("请输入你要修改的正确姓名：")  # 在对应编号下修改的信息
                    modify_flag = 1
                elif num1 == 2:
                    card_infors[sign - 1]["qq"] = input("请输入你要修改的正确QQ")
                    modify_flag = 1
                elif num1 == 3:
                    card_infors[sign - 1]["high"] = input("请输入你要修改的正确身高")
                    modify_flag = 1
                elif num1 == 4:
                    card_infors[sign - 1]["addr"] = input("请输入你要需要的正确地址")
                    modify_flag = 1
                elif num1 == 5:
                    card_infors[sign - 1]["telephon"] = input("请输入你要修改的正确电话号码")
                    modify_flag = 1
                elif num1 == 6:
                    break
                else:
                    print("输入有误，请重新输入")
                if modify_flag == 1:
                    print("修改成功")
                    break
            break  # 停止查找循环

def find_card_name():
    """查找输入的名字对应的名片"""
    # global card_infors
    find_name = input("请输入要查找的姓名：")
    find_flag = 0  # 默认表示没有找到
    for temp in card_infors:
        if find_name == temp["name"]:
            print("%s\t%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['high'], temp['addr'], temp['telephon']))
            find_flag = 1  # 表示找到了
            break  # 使找到后停止for循环
    # 判断是否找到了
    if find_flag == 0:
        print("没有你要查找的姓名")

def print_card():
    """输出所有的名片"""
    #global card_infors
    print("姓名\tQQ\t身高\t住址\t联系方式")
    for temp in card_infors:
        print("%s\t%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['high'], temp['addr'], temp['telephon']))

def sava_2_file():
    """把已经添加的信息保存到文件中"""
    f = open("backup.data","w") #.data是自己打的，可以自己定义

    f.write(str(card_infors))

    f.close()

def load_infor():
    global card_infors
    try:  #当原文件不存在时，跳过这个错误，后面保存的时候会新建一个文件
        f = open("backup.data")

        card_infors = eval(f.read()) #eval() 之前是什么格式，eval就转换成什么格式

        f.close()
    except Exception:
        pass

def main():
    """完成对整个程序的控制"""

    #回复家在之前的数据到程序中
    load_infor()
    #1.打印功能提示
    print_menu()   #改程序的时候，改一点 试用一次，不要全改完了再用

    while True:
        # 2.获取用户输入
        num = int(input("请输入操作序号(只能是数字)："))
        #3.根据用户的数据执行相应功能
        if num == 1:
            add_new_card_infor()

        elif num == 2:
            dele_name()

        elif num == 3:
            modify_name_card()

        elif num == 4:
            find_card_name()

        elif num == 5:
            print_card()
        elif num ==6:
            sava_2_file()
        elif num == 7:
            break
        else:
            print("请输入正确的操作序号")
        print("")
if __name__ == "__main__":
    #调用主函数
    main()