class Node(object):
    """结点"""
    def __init__(self,item):
        self.elem = item
        self.next = None #指向后继结点
        self.prev = None #指向前驱结点

class DoubleLinkList(object):
    """双链表"""
    def __init__(self, node=None): #链表头 私有属性head
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        cur = self.__head
        # count 用来记录数量
        count = 0
        while cur != None:
            count+=1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        #cur 游标，用来移动遍历节点
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self,item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head #先走下面这步会导致丢失整个单链表
        self.__head = node #指向node而不是node.elem
        node.next.prev = node

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
            node.prev = cur

    def insert(self,pos,item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cur =self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
                #当循环退出后，cur指向pos位置
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self,item):
        """删除节点"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                #先判断此节点是否是头节点
                #头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        #判断链表是否只有一个节点
                        cur.next.prev = cur.prev
                else:
                    cur.prev.next = cur.next
                    if cur.next: #判断是否是尾节点 尾节点的cur.next == None 没有prev
                        cur.next.prev = cur.prev
                break #删完了之后退出循环
            else:
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

if __name__ == "__main__":
    l1 = DoubleLinkList()
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
    l1.travel() #9 8 1 100 2 3 4 5 6