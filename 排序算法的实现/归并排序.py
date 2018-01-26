def quick_sork(alist, first, last):
    """快速排序"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first #起始下标
    high = last #末尾下标
    while low < high:
        while low < high and alist[high] >= mid_value: #相遇之后就不能往左走了
            high -= 1 # high往左走一步
        alist[low] = alist[high] #low和high相等的时候这个没有意义 没有影响

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value #这个时候low和high相等

    #对low左边的列表执行快速排序
    quick_sork(alist, first, low-1) #递归
    #对low右边的列表进行快速排序
    quick_sork(alist, low+1, last) #右边的用这个 然后代入进入 这个时候 右边的代入进去得到的左边的first=low+1(旧)
    #右边的 low+1 =一个新的low+1(新)

if __name__ == "__main__":
    li = [42,2,45,677,33,22,11,33,79]
    print(li)
    quick_sork(li, 0, len(li)-1)
    print(li)

#[42, 2, 45, 677, 33, 22, 11, 33, 79]
#[2, 11, 22, 33, 33, 42, 45, 79, 677]