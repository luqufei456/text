def binary_search(alist, item):
    """二分查找"""
    n = len(alist)
    if n >= 1:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)  # 要返回一个返回值
        else:
            return binary_search(alist[mid + 1:], item)
    return False


if __name__ == "__main__":
    li = [11, 22, 33, 44, 55, 66, 77]
    print(binary_search(li, 55))
    print(binary_search(li, 100))

# True
# False