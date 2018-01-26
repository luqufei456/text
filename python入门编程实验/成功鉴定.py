#判断性别
sex = input("请输入你的性别：")
if sex == "男":
    money = int(input("请输入你的财产(万)："))
    high = int(input("请输入你的身高(cm)："))
    face = input("你帅吗")
    if money >=100 and high >= 180 and face == "帅":
        print("高富帅")
    else:
        print("穷挫矮")
else: #性别为女性时
    money = int(input("请输入你的财产(万)："))
    color = input("你白吗")
    face = input("你美吗")
    if money >= 100 and color == "白" and face == "美":
        print("白富美")