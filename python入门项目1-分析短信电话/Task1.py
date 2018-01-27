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
countnum = set()
for nums in texts:
    if nums[0] not in countnum:
        countnum.add(nums[0])
    else:
        pass
    if nums[1] not in countnum:
        countnum.add(nums[1])
    else:
        pass
for nums in calls:
    if nums[0] not in countnum:
        countnum.add(nums[0])
    else:
        pass
    if nums[1] not in countnum:
        countnum.add(nums[1])
    else:
        pass

print("There are {} different telephone numbers in the records.".format(len(countnum)))
"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""""
