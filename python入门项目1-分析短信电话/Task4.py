"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
Tui_xiao_nums = []
Bei_bo=[]
Bei_fa=[]
Fa_txt=[]
for temp in calls:
    if temp[1] not in Bei_bo:
        Bei_bo.append(temp[1])
for temp in texts:
    if temp[1] not in Bei_fa:
        Bei_fa.append(temp[1])
for temp in texts:
    if temp[0] not in Fa_txt:
        Fa_txt.append(temp[0])
for temp in calls:
    if temp[0] not in Bei_fa and temp[0] not in Bei_bo and temp[0] not in Fa_txt and temp[0] not in Tui_xiao_nums:
        Tui_xiao_nums.append(temp[0])
Tui_xiao_nums=sorted(Tui_xiao_nums)
def list_num(list):
    for num in list:
        print(num)
print("These numbers could be telemarketers: ")
list_num(Tui_xiao_nums)
"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

