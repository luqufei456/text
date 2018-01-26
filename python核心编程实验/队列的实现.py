class Queue(object):
    """队列"""

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列中添加一个item"""
        self.__list.append(item)
        # self.__list.insert(0, item) #根据实际应用去选择

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)
        # self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())

# 1
# 2
# 3
# 4