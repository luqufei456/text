def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(0, n-1): #一共有n个 那么就要比较n-1次留下的一个就是最大的不用比较 下标为0
        min_index = j #设置一个比较的初始下标 用于替换成比较中最小的值
        for i in range(1+j, n): #第一次要比较n-1次 从下标为1的地方开始 第二次从下标为2的地方开始
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
#相当于把一个列表分成两部分 一部分放比较出来的最小值 另一部分比较

if __name__ == "__main__":
    li = [42,2,45,677,33,22,11,33,79]
    print(li)
    select_sort(li)
    print(li)

#[42, 2, 45, 677, 33, 22, 11, 33, 79]
#[2, 11, 22, 33, 33, 42, 45, 79, 677]