def binary_search(alist, item):
    """二分查找"""
    n = len(alist)
    first = 0  # 定义两个下标
    last = n - 1
    while first <= last:  # == 的时候 还有一个mid可以比较
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1  # 改变末尾下标值
        else:
            first = mid + 1  # 改版初始下标值
    return False


if __name__ == "__main__":
    li = [11, 22, 33, 44, 55, 66, 77]
    print(binary_search(li, 55))
    print(binary_search(li, 100))

# True
# False