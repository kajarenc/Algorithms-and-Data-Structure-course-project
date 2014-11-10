class otrezok:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __str__(self):
        return(str(self.start)+"---"+str(self.end))
    def getStart(self):
        return self.start
    def getEnd(self):
        return self.end
def SortByStart(otrezok):
    return otrezok.getStart()
def howManyTimes(point,otrezoks):
    times = 0
    i = 0
    while(i<len(otrezoks) and otrezoks[i].getStart()<=point):
        if(otrezoks[i].getEnd()>=point):
            times +=1
        i+=1
    return times
nmInput = input()
arrayInputTokens = nmInput.split()

n = int(arrayInputTokens[0])
m = int(arrayInputTokens[1])
otrezoks = []
points = []
for item in range(0,n):
    otrInput = input()
    arrInput = otrInput.split()
    otrezoks.append(otrezok(int(arrInput[0]),int(arrInput[1])))
pointInput = input()
pointsToken = pointInput.split()
points = [int(item) for item in pointsToken]
otrezoks.sort(key = SortByStart)

outputStr = ""
for point in points:
    strToAdd = str(howManyTimes(point,otrezoks))+" "
    outputStr+=strToAdd
print (outputStr)

