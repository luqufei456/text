class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

# node = Node(100)
class SingleCycleLinkList(object):
    """单链表"""
    def __init__(self, node=None): #链表头 私有属性head
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty(): #如果是空链表返回0
            return 0
        cur = self.__head
        # count 用来记录数量
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty(): #如果是空链表 直接返回
            return
        #cur 游标，用来移动遍历节点
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        #退出循环，cur指向尾节点，但尾节点的元素未打印
        print(cur.elem)

    def add(self,item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head #先走下面这步会导致丢失整个单链表
        self.__head = node #指向node而不是node.elem

    def append(self,item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <=0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
                #当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                #先判断此节点是否是头节点
                #头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break #删完了之后退出循环
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None: #cur.next的话比较不了最后一个
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False