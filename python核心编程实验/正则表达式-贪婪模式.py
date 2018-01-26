import re

s = """<div>
<p>岗位职责:</p>
<p>完成推荐算法。。。</p>
"""
re.sub(r"<.+>", "", s) # /n /n
#因为正则表达式默认处于贪婪模式 一行里面 只要符合"."的定义 >也会被当成"."吃掉 然后会一直往后走 直到碰见换行会返回一个\n

s = "This is a number 234-235-22-423"
r = re.match(r"(.+)(\d+-\d+-\d+-\d+)", s)
print(r.group(1)) # This is a number 23
print(r.group(2)) # 4-235-22-423
#为什么呢 因为正则表达式是贪婪的 只要符合就会一直往下走  然后\d是要求只要有一个 所以只留了4-给r.group(2)
#从头往后一直走 直到遇到满足后面一个规则的最小情况停止

#怎么关闭贪婪模式
r = re.match(r"(.+?)(\d+-\d+-\d+-\d+)", s) #在后面加上一个? 就能关闭"+"的贪婪模式 之后就是满足后面的规则而尽可能少的吃东西
print(r.group(1)) # This is a number
print(r.group(2)) # 234-235-22-423

#例子：
re.match(r"aa(\d+)", "aa2343ddd").group(1) #2343
re.match(r"aa(\d+?)", "aa2343ddd").group(1) #2
re.match(r"aa(\d+)ddd", "aa2343ddd").group(1) #2343
re.match(r"aa(\d+)ddd", "aa2343ddd").group(1) #2343