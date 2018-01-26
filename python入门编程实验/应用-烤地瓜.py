class SweetPotato:  #定义一个类烤地瓜

    def __init__(self):  #设置属性默认值
        self.cookedString = "生的"  #默认值是生的
        self.cookedLevel = 0  #用于保存烤的时间
        self.seasoning = []  #添加多个元素

    def __str__(self):  #决定了打印出来的内容
        return "地瓜的状态：%s(%d),添加的佐料有：%s"%(self.cookedString,self.cookedLevel,str(self.seasoning))

    def cook(self,cooked_time):
        self.cookedLevel += cooked_time   #将烤的时间加入属性中  因为方法内的变量不能保存 属性可以
        if self.cookedLevel >= 0 and self.cookedLevel<3:
            self.cookedString = "生的"
        elif self.cookedLevel >= 3 and self.cookedLevel<5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel >= 5 and self.cookedLevel<8:
            self.cookedString = "熟透了"
        else:
            self.cookedString = "烤成木炭"

    def addSeasoning(self,item):
        self.seasoning.append(item)


#创建了一个地瓜对象
di_gua = SweetPotato()
print(di_gua)
#开始烤地瓜
di_gua.addSeasoning("黑椒粉") #添加佐料
di_gua.cook(1)  #烤一分钟
print(di_gua)