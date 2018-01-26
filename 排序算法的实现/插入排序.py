def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1, n):  # 第一次比较从下标为1的地方开始
        i = j  # i代表内层循环起始下标
        # 内层循环代表的是 执行从右边的无序序列中取第一个即i位置然后和左边的有序序列进行比较的过程
        while i > 0:  # 当i=0时 说明比较到头了
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:  # 插入算法的优化
                break  # 如果说比前面的大或者相等，就可以退出循环了


if __name__ == "__main__":
    li = [42, 2, 45, 677, 33, 22, 11, 33, 79]
    print(li)
    insert_sort(li)
    print(li)

# [42, 2, 45, 677, 33, 22, 11, 33, 79]
# [2, 11, 22, 33, 33, 42, 45, 79, 677]