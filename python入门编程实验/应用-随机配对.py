import random  #引入一个模块random

man = []  #定义一个空的列表用来存储输入的姓名


def input_man():
    man.append(input("input man: "))  #输入语句


def get_man():
    thisman = man[int(random.randint(0, man.__len__() - 1))]  #利用len()测出列表的字节然后利用random工具箱随机取值，然后利用下标取出随机出的对应名字引用给thisman
    man.remove(thisman)   #在列表中删除已经取出的名字，防止二次选中
    return thisman   #保存thisman的值


if __name__ == "__main__":  #表示这是一个主函数
    while not "end" in man:  #当"end"不在列表man中时
        input_man()  #调用input_man()
    man.remove("end")  #当"end"在列表中时，删除"end"
    while not man.__len__() == 0:  #利用len()测出，当列表中还有字节时（即还存有姓名时
        if man.__len__() % 2 == 0:  #当列表的长度除以二余数为0时 即列表中的名字为双数
            print(get_man() + ":" + get_man())  #输出2个姓名 都是随机出的
        else:   #当列表中的名字为奇数时
            print(get_man() + " is bye")  #随机输出一个姓名 若输入了奇数个姓名，则先输出这