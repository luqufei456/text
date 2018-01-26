ticket = input("是否有车票(1(有)or0(没有))")  # 1表示有车票 0表示没有

# 先判断是否有车票
if ticket == "1":
    print("通过了车票检测，进入车站，等候安检")
    knife_Lenght = int(input("输入管制刀具长度(cm)"))  # 刀具长度(cm)

    # 判断刀具长度是否合法
    if knife_Lenght <= 10:
        # 该段if else语句属于上个if语句 上个语句通过才执行该if else语句
        print("通过安检，进入候车厅")
    else:
        print("安检不通过，等待公安处理")

else:
    print("没有车票，需要补票")