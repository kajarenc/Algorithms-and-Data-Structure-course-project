__author__ = 'Java'
k = input()
nextInput = input()
nextInputTokens = nextInput.split()
deSortArray = []
for item in nextInputTokens:
   deSortArray.append(int(item))
def mySuperFunction(deSortedArray):
    counts = [0 for i in range(0,10)]

    for item in deSortedArray:
        counts[item%10]+=1
    outputStr = ""
    for i in range(1,10):
        for j in range(0,counts[i]):
            outputStr +=str(i)
            outputStr+=' '
    for j in range(0,counts[0]):
        outputStr+=str(10)
        outputStr+= ' '
    return outputStr



print(mySuperFunction(deSortArray))








