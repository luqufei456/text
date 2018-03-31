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