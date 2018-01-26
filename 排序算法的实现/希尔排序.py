def shell_sort(alist):
    """希尔排序"""
    #假设n=9
    n = len(alist)
    # gap=4
    gap = n//2 #取整数
    while gap >= 1:
        # 插入算法，与普通的插入算法的区别就是gap步长 如果不取1 会丢掉最后一次插入排序
        for j in range(gap, n):
            # j = [gap, gap+1, gap+2, gap+3, ..., n-1]
            i = j
            while i> 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短gap步长
        gap //= 2

if __name__ == "__main__":
    li = [42,2,45,677,33,22,11,33,79]
    print(li)
    shell_sort(li)
    print(li)

#[42, 2, 45, 677, 33, 22, 11, 33, 79]
#[2, 11, 22, 33, 33, 42, 45, 79, 677]