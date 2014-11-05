__author__ = 'Java'


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def extractMax(self):
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.siftDown(1)
        return retVal


    def siftDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.siftUp(self.currentSize)

    def siftUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2


myHeap = BinHeap()

kInput = input()
kInt = int(kInput)
for i in range(0, kInt):
    usInput = input()
    usInputTokens = usInput.split()
    if (str(usInputTokens[0]) == "Insert"):
        myHeap.insert(int(str(usInputTokens[1])))
    elif (str(usInputTokens[0]) == "Extract"):
        print(myHeap.extractMax())

















