def listCompare(list1, list2):
    equalCount = 0
    totalCount = 0
    shortListSize = min(len(list1), len(list2))
    for i in range(shortListSize):
        totalCount += 1
        if isinstance(list1[i], str) and isinstance(list2[i], str):
            if list1[i].lower() == list2[i].lower():
                equalCount += 1
        elif list1[i] == list2[i]:
            equalCount += 1
    if len(list1) > len(list2):
        totalCount += len(list1) - len(list2)
    elif len(list2) > len(list1):
        totalCount += len(list2) - len(list1)
    if totalCount == 0:
        return "The lists are 0% equal"
    else:
        percentage = (equalCount / totalCount) * 100
        return "The lists are " + str(percentage) + "% equal"

print(listCompare([1,2,3,'Fred'], [1,2,'3', 3,4,5,6,5,6,7])) 
print(listCompare([1,2.0,3,'fred'], [1,2,3,'Fred']))