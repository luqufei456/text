#批量删除输入的部分文件名
import os
#1.获取要重命名的文件夹的名字
folder_name = input("请输入要重命名的文件夹：")
_name = input("请输入想要删除的部分文件名：")
#2.获取指定文件夹中所有的文件名
file_names = os.listdir(folder_name)

#改变操作路径
os.chdir(folder_name)  #使操作路径到需要操作的文件夹中

#3.重命名
for name in file_names:
    print(name)
    new_name = name.replace(_name,"")  #替换想要删除的部分文件名为空格
    os.rename(name,new_name)  #前面为旧文件名，后面为新文件名