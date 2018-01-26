def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(0, n - 1):
        count = 0
        for i in range(0, n - 1 - j):  # 下标从0开始 最后一个是n-1 判断到n-2的地方 range取不到n-1
            # 班长从头走到尾
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:  # 优化 当一次循环没有换值 直接退出
            return

        # 第一次 i0 -- n-2 range(0, n-1) j=0  第一次执行n-1次 第二次执行n-2次 类推 然后因为j初始值为0  i也是0 所以n-1-j


# 第二次 i0 -- n-3 range(0, n-1-1) j=1
# 第三次 i0 -- n-4 range(0, n-1-2) j=2
#    range(0, n-1-j)

if __name__ == "__main__":
    li = [42, 2, 45, 677, 33, 22, 11, 33, 79]
    print(li)
    bubble_sort(li)
    print(li)

# [42, 2, 45, 677, 33, 22, 11, 33, 79]
# [2, 11, 22, 33, 33, 42, 45, 79, 677]