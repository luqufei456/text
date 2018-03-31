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

def func_arg(arg):
    def func(functionName):
        def func_in():
            print("----记录日志--arg=%s--"%arg) #arg在这个装饰器中相当于全局变量一样，整个装饰器都可以调用
            if arg == "poi": #起到一个区分的效果
                functionName()
                functionName()
            else:
                functionName()
        return func_in
    return func

#1.先执行func_arg("poi")函数，这个函数return 的结果是func这个函数的引用 引用func 但不会执行 要在后面调用test()这种才执行
#2.@func  #如果内部只有一层函数 就无法构成 @func这样的装饰器了，就会报错
#3.使用@func对test进行装饰
@func_arg("poi")
def test():
    print("----test----")

#带有参数的装饰器，能够起到在运行时，有不同的功能
@func_arg("chunjue")
def test2():
    print("----test2----")

test()
test2()