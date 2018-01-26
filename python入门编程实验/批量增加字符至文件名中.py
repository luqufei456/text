#批量增加字符进文件名中
import os
#1.获取要重命名的文件夹的名字
folder_name = input("请输入要重命名的文件夹：")

#2.获取指定文件夹中所有的文件名
file_names = os.listdir(folder_name)

#改变操作路径
#os.chdir(folder_name)  #使操作路径到需要操作的文件夹中

#3.重命名
for name in file_names:
    print(name)
    old_file_name = folder_name +"/"+name  #表示folder_name文件夹 下的 name "/"表示目录下 的意思
    new_file_name = folder_name +"/"+"[yiran]-"+name
    os.rename(old_file_name,new_file_name)
    #os.rename(name,"[yiran]-"+name)  #前面为旧文件名，后面为新文件名