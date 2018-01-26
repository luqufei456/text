from multiprocessing import Pool
import time
import os


def test():
    print("---进程池中的进程---pid=%d,ppid=%d--" % (os.getpid(), os.getppid()))
    for i in range(3):
        print("---%d---" % i)
        time.sleep(1)
    return "haha"  # 保存的返回值给了主进程


def test2(args):
    print("---callback func--pid=%d" % os.getpid())
    print("---callback func--args=%s" % args)  # 打印出的是子进程保存的返回值 由主进程输送进来


pool = Pool(3)
pool.apply_async(func=test, callback=test2)  # func=test 等价于test。 callback意思是回调 子进程结束后，
# 打断主进程正在执行的任务去执行回调指向的函数，做完之后再做之前在做的事情

while True:
    print("----主进程-pid=%d" % os.getpid())

# 异步的优点是，不用等待任务产生，该做什么做什么，任务产生后再去做 不会浪费时间