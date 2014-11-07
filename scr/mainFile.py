__author__ = 'Java'

kInput = input()
arrayInput = input()
arrayInputTokens = arrayInput.split()
arrayBeforeSort = [int(item) for item in arrayInputTokens]


def sortAndCountInversions(nonSortArray):
    if len(nonSortArray) <= 1:
        print("O_I")
        return 0
    blueArray = [item for item in nonSortArray[:len(nonSortArray) // 2]]
    greenArray = [item for item in nonSortArray[len(nonSortArray) // 2:len(nonSortArray)]]

    print("Blue array before sorting:"+str(blueArray))
    print("Green array before sorting:"+str(greenArray))

    inversionsInBlue = sortAndCountInversions(blueArray)
    inversionsInGreen = sortAndCountInversions(greenArray)

    print("Blue array after sorting:"+str(blueArray))
    print("Green array after sorting:"+str(greenArray))

    sortedArray = []
    blueGreenInversionsCount = 0
    i = 0
    j = 0

    for k in range(0, len(blueArray)+len(greenArray)):
        if i !=len(blueArray) and blueArray[i] <= greenArray[j]:
            sortedArray.append(blueArray[i])
            i += 1
        else:
            sortedArray.append(greenArray[j])
            blueGreenInversionsCount += (len(blueArray) - i)
            j += 1
    print("Number in nonsortedArray:"+str(nonSortArray)+"is "+str(inversionsInBlue + inversionsInGreen + blueGreenInversionsCount))
    nonSortArray = sortedArray
    return inversionsInBlue + inversionsInGreen + blueGreenInversionsCount

print("------------------------------------------------------------------------")
print(sortAndCountInversions(arrayBeforeSort))











