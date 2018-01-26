#使用copy模块的copy功能的时候，它会根据当前拷贝的数据类型是可变类型还是不可变类型采取不同的处理方式

import copy

a = [1,2,3]
b = [4,5,6]
c = (a,b)
e = copy.copy(c)
print(id(c))
print(id(e))
#id(c) == id(e)
#当拷贝的对象是不可变类型时候，直接不拷贝值

a.append(4)
print(id(c))
print(id(e)) #指向的内存空间也没有变化
#c[0] == e[0] #[1,2,3,4]