class Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area  #面积
        self.info = new_info  #户型
        self.addr = new_addr  #地址
        self.left_area = new_area  #可用面积
        self.contain_items = []   #保存添加物品的名字

    def __str__(self):
        msg = "房子的面积是：%d，可用面积是%d，户型是：%s，地址是：%s"%(self.area,self.left_area,self.info,self.addr)
        msg += "当前房中的物品有：%s"%(str(self.contain_items))  #因为列表不能用%s输出 所以转成字符串
        return msg   #保存返回值

    def add_item(self,item): #添加一个物品
        #self.left_area -= item.area  #通过引用得出床的面积
        #self.contain_items.append(item.name)  #通过引用将床的名字添加到列表中
        self.left_area -= item.get_area()  #通过这种办法 如果权限不够 不能得到值 一般用这种
        self.contain_items.append(item.get_name())  #self指向房子，item指向床

class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "%s占用的面积是：%d"%(self.name,self.area)

    def get_area(self):
        return self.area   #设置获得数据的条件

    def get_name(self):
        return self.name

fangzi = Home(129,"三室一厅","北京市 朝阳区 长安街 666号")
print(fangzi)

bed1 = Bed("席梦思",4)
fangzi.add_item(bed1)
print(fangzi)

bed2 = Bed("三人床",6)
fangzi.add_item(bed2)
print(fangzi)