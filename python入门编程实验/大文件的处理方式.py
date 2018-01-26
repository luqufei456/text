# 1.获取用户要复制的文件名
old_file_name = input("请输入想要复制的文件名：")

# 2.打开要复制的文件 old_file_name 本身就是字符串不用打引号
old_file = open(old_file_name, "r")
# new_file_name = "[复件]"+old_file_name
position = old_file_name.rfind(".")
new_file_name = old_file_name[:position] + "[复件]" + old_file_name[position:]  # 表示找出.的下标然后在.前加上[复件]，命名给new_file_name

# 3.新建一个文件
# new_file = open("test1.py","w")
new_file = open(new_file_name, "w")

# 4.定义一个string引用从旧文件中读取的数据，并写入到新文件中
while True:  # 使用while循环将old_file中的数据按1024字节一次分多次写入到new_file中，当string字节数为0时 表示读取完毕 终止循环
    string = old_file.read(1024)
    if len(string) == 0:
        break

    new_file.write(string)

# 5.关闭2个文件
old_file.close()
new_file.close()