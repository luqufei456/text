import os
import time

g_num = 100

#父进程
ret = os.fork()
if ret == 0:
    #子进程
    print("---1---")
else:
    #父进程
    print("---2---")

#父子进程  然后父子进程分别隔开再分进程
ret = os.fork()
if ret == 0:
    print("---11---")
else:
    print("---22---")

# 1 2 出现一次  11 22各出现2次 遇到第二个ret = os,fork()会再分一个子进程
# 然后前面也是2个进程分开遇到这一步，相当于分叉2次 1进程变2  2个变4