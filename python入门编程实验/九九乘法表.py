i = 1
while i <=9:

    j = 1
    while j<=i:

        print("%d*%d=%d\t"%(j,i,j*i),end="")#end="" 使其不换行 /t相当于tab 自动对齐的功能
        #print("x*y=z",end="")先设出xyz再用代码中的变量替代
        j = j+1

    print("")#使嵌套中的while循环完成后换行

    i=i+1