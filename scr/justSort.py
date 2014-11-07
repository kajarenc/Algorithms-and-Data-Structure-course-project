__author__ = 'Java'

kInput = input()
kInt = int(kInput)
arrayInput = input()
arrayInputTokens = arrayInput.split()
arrayForSort = [int(item) for item in arrayInputTokens]
arrayForSort.sort()
for itm in arrayForSort:
    print(str(itm)+' ')