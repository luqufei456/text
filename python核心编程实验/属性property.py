#1
class Test(object):
    def __init__(self):
        self.__num = 100

    def setNum(self,newNum):
        print("-----setter-----")
        self.__num = newNum

    def getNum(self):
        print("-----getter-----")
        return self.__num
    num = property(getNum,setNum) #将两个方法保存 返回值给num，不能写小括号，只能写方法名

t = Test()


t.num = 200  #相当于调用了t.setNum(200)
print(t.num)  #相当于调用了t.getNum()
print("-"*50)
# 注意点
# t.num 到底是调用getNum()还是setNum(),要根据实际场景来判断
# 1. 如果是给t.num赋值 那么一定调用setNum()
# 2. 如果是获取t.num的值，那么就一定调用getNum()

# property的作用：相当于把方法进行了封装，开发者在对属性设置数据的时候更方便

#2
class Test(object):
    def __init__(self):
        self.__num = 100

    @property  # 默认为gettet方法 property下面的方法名叫什么 外面就用什么
    def num(self):
        print("-----getter-----")
        return self.__num

    @num.setter  # 根据上面的方法名来命名 这里是表示可写
    def num(self, newNum):
        print("-----setter-----")
        self.__num = newNum

t = Test()

t.num = 200  #相当于调用了t.setNum(200)

print(t.num)  #相当于调用了t.getNum()

# @property 表示只读，同时有@property和@x.setter表示可读可写
# 同时有@property和@x.setter和@x.deleter表示可读可写可删除。

