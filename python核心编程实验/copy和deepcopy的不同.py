import copy

a = [1,2,3]
b = [4,5,6]
c = [a,b]
e = copy.copy(c)

a.append(4)
print(c[0]) #[1,2,3,4]
print(e[0]) #[1,2,3,4]

id(c) != id(e)

#deepcopy:里面还有引用，就接着拷值
#copy:只拷第一次值