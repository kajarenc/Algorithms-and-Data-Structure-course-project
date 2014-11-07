kInput = input()
arrayInput = input()
arrayInputTokens = arrayInput.split()
arrayBeforeSort = [int(item) for item in arrayInputTokens]

def sortAndCountInversions(nonSortArray):
    if len(nonSortArray) <= 1:
        return 0
    if len(nonSortArray) == 2:
        if nonSortArray[0]>nonSortArray[1]:
            nonSortArray.sort()
            return 1
        else:
            return 0
    print("NON SORTED ARRAY"+str(nonSortArray))

    blueArray = nonSortArray[:(len(nonSortArray)+1) // 2]
    greenArray = nonSortArray[(len(nonSortArray)+1) // 2:]

    print("NON SORTED BLUE ARRAY"+str(blueArray))
    print("NON SORTED GREEN ARRAY"+str(greenArray))

    inversionsInBlue = sortAndCountInversions(blueArray)
    inversionsInGreen = sortAndCountInversions(greenArray)

    sortedArray = []
    blueGreenInversionsCount = 0
    i = 0
    j = 0
    # blueArray.sort()
    # greenArray.sort()
    print("SORTED BLUEARRAY"+str(blueArray))
    print("SORTED GREENARRAY"+str(greenArray))
    for k in range(0,len(nonSortArray)):
        if(i == len(blueArray)):
            for item in greenArray[j:]:
                sortedArray.append(item)
            break
        if(j == len(greenArray)):
            for item in blueArray[i:]:
                sortedArray.append(item)
            break

        if blueArray[i] <= greenArray[j]:  #"""i<len(blueArray)) and"""
            sortedArray.append(blueArray[i])
            i += 1
        else:
            sortedArray.append(greenArray[j])
            blueGreenInversionsCount += (len(blueArray) - i)
            j += 1
    print("SortedARRAY:"+str(sortedArray));

    nonSortArray.clear()
    for item in sortedArray:
         nonSortArray.append(item)
    return inversionsInBlue + inversionsInGreen + blueGreenInversionsCount

print(sortAndCountInversions(arrayBeforeSort))












