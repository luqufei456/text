from timeit import Timer

#li1 = [1,2]
#li2 = [3,4]
#li = li1 + li2
#li = [i for i in range(10000)] #列表生成器
#li = list(range(10000)) #把可迭代对象转换成列表

def test1():
    li = []
    for i in range(10000):
        li.append(i)

def test2():
    li = []
    for i in range(10000):
        li += [li]  #在旧列表操作  python中x+=y 不等于 x=x+y 优化了

def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10000))

def test5():
    li = []
    for i in range(10000):
        li.extend([i]) #两个列表的合并

timer1 = Timer(stmt="test1()", setup="from __main__ import test1") #因为运行的时候是__main__
print("append:", timer1.timeit(number=1000))

timer2 = Timer(stmt="test2()", setup="from __main__ import test2") #因为运行的时候是__main__
print("+:", timer2.timeit(number=1000))

timer3 = Timer(stmt="test3()", setup="from __main__ import test3") #因为运行的时候是__main__
print("[i for i in range()]", timer3.timeit(number=1000))

timer4 = Timer(stmt="test4()", setup="from __main__ import test4") #因为运行的时候是__main__
print("list(range())", timer4.timeit(number=1000))

timer5 = Timer(stmt="test5()", setup="from __main__ import test5") #因为运行的时候是__main__
print("extend:", timer5.timeit(number=1000))

#append: 0.9205941045544253
#+: 0.8870971880507552
#[i for i in range()] 0.43950306296901265
#list(range()) 0.2953371465269248
#extend: 1.436412968572677

def test5():
    li = []
    for i in range(10000):
        li.append(i) #从尾加

def test6():
    li = []
    for i in range(10000):
        li.insert(0, i) #从下表为0的地方开始添加 ，即从头加

timer5 = Timer(stmt="test5()", setup="from __main__ import test5") #因为运行的时候是__main__
print("append:", timer5.timeit(number=1000))

timer6 = Timer(stmt="test6()", setup="from __main__ import test6") #因为运行的时候是__main__
print("insert:", timer6.timeit(number=1000))

#append: 0.9198536548888738
#insert: 28.73487539918301