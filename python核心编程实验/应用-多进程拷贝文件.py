from multiprocessing import Pool, Manager
import os

def copyFileTask(name,oldFolderName,newFolderName):
    "完成copy一个文件的功能"
    #print(name) #调试
    fr = open(oldFolderName+"/"+name)
    fw = open(newFolderName+"/"+name,"w")
    #print("-----") #调试
    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(name)

def main():
    #0.获取用户要copy的文件夹的名字
    oldFolderName = input("请输入文件夹的名字：")

    #1.创建一个文件夹
    newFolderName = oldFolderName+"-复件"
    #print(newFolderName)
    os.mkdir(newFolderName)

    #2.获取old文件夹中所有的文件名
    fileNames = os.listdir(oldFolderName)
    #print(fileNames)

    #3.使用多进程的方式copy 原文件夹中的所有文件到新文件夹中
    pool = Pool(5)
    queue = Manager().Queue()

    for name in fileNames:
        pool.apply_async(copyFileTask,args=(name,oldFolderName,newFolderName,queue)) #不加逗号就不是元组 传不进去

    num = 0
    allNum = len(fileNames)
    while num<allNum: #如果写相同 拷贝完了还在运行
        queue.get()
        num += 1
        copyRate = num/allNum
        print("\rcopy的进度是：%.2f%%"%(copyRate*100),end="") #\r默认将输出返回到第一个指针，这样的话，后面的内容会覆盖前面的内容
        #end="" 输出后不换行  %.2f是float后的小数只输出两位   %%就是转换成百分比
        #if num == allNum:
            #break
    print("\n已完成拷贝")
    #pool.close() #因为主进程结束后程序就结束了，这里是为了防止子进程还没生效就被结束
    #pool.join()

if __name__ == "__main__":
    main()