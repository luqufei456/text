dict = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

def most_prolific(dict):
    nums = []
    a = {} #年份与出专辑次数组成的字典
    years = []#保存dict中的值
    num = []#保存a中的值，即每年初专辑的次数组成列表
    for album_title in dict:
        years.append(dict[album_title])
    print(years)
    for year in years:
        if years.count(year)>0:#当该年出唱片的次数大于0时
            a[year] = years.count(year) #添加到字典
    print(a)
    for temp in a:
        num.append(a[temp]) #将a字典中的值添加到num中
    num.sort() #排序
    print(num)
    max_val = num[-1] #得出最大的值
    print(max_val)
    for year in a:
        if (a.get(year)==max_val): #当该年的值与最大的值相同时
            nums.append(year) #添加该年到nums
    if len(nums) == 1: #当nums列表长度为1时，保存下标为0的元素
        return nums[0]
    else:
        return nums #当ums列表长度不为1时，保存列表

print(most_prolific(dict))