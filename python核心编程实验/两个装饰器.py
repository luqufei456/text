#定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        print("----1----")
        return "<b>" + fn() + "</b>"
    return wrapped

#定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        print("----2----")
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
@makeItalic
def test3():
    print("----3----")
    return "hello word-3"

print(test3())

#----1---- 先调用makeBold里的wrapped 然后里面调用fn时，下面又是一个装饰器，于是去调用makeItalic里的wrapped
#----2---- 然后第二个装饰器里的函数调用test3
#----3---- test3被第二个装饰器调用，先运行第二个装饰器的return 再返回给第一个装饰器调用
#<b><i>hello word-3</i></b>

#强调：
def w1(func):
    print("---正在装饰1---")
    def inner():
        print("---正在验证权限1---")
        return func() + " chunjue"
    return inner

def w2(func):
    print("---正在装饰2---")
    def inner():
        print("---正在验证权限2---")
        return func() + " yiran"
    return inner

@w1  # 只要python解释器执行到了这个代码，就会自动装饰，而不是等到调用时再装饰
@w2  # 因为w1下面的不是函数 所以要先执行w2才能装饰 所以先装饰了w2，相当于暂停w1
def f1():
    return "baka"

# 在调用f1之前，已经进行装饰了，调用是调用的装饰之后的结果  倒着装饰，正着调用
print(f1())

# ---正在装饰2---
# ---正在装饰1---
# ---正在验证权限1---
# ---正在验证权限2---
# baka yiran chunjue