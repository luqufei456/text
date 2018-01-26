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
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            #退出循环之后 cur指向尾节点
            node.next = self.__head #先走下面这步会导致丢失整个单链表
            self.__head = node #指向node而不是node.elem
            #cur.next = node
            cur.next = self.__head

    def append(self,item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # node.next = self.__head
            node.next = cur.next
            cur.next = node

    def insert(self,pos,item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <=0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else: #在中间位置插入的时候 和单链表一个效果 不需要更改
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
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head: #当cur指向尾节点的时候退出了循环
            if cur.elem == item:
                #先判断此节点是否是头节点
                #头节点
                if cur == self.__head:
                    #头节点的情况
                    #找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                    #self.__head = cur.next
                else: #中间节点
                    pre.next = cur.next
                return #删完了之后退出整个函数 用brak 下面还有个if判断
            else:
                pre = cur
                cur = cur.next
        #退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                pre.next = cur.next
                #pre.next = self.__head


    def search(self,item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        #出循环之后cur指向尾节点
        if cur.elem == item:
            return True
        return False

if __name__ == "__main__":
    l1 = SingleCycleLinkList()
    print(l1.is_empty())
    print(l1.length())

    l1.append(1)
    print(l1.is_empty())
    print(l1.length())

    l1.append(2)
    l1.add(8)
    l1.append(3)
    l1.append(4)
    l1.append(5)
    l1.append(6)
    #8 1 2 3 4 5 6
    l1.insert(-1, 9)
    l1.travel()#9 8 1 2 3 4 5 6
    l1.insert(3, 100)
    l1.travel()#9 8 1 100 2 3 4 5 6
    l1.insert(10, 200)
    l1.travel()#9 8 1 100 2 3 4 5 6 200
    l1.remove(200)
    l1.remove(9)
    l1.travel() #8 1 100 2 3 4 5 6