# Merge short

def shortMyArry(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        shortMyArry(leftArr)
        shortMyArry(rightArr)

        leftIndex = rightIndex = mainIndex = 0

        while leftIndex < len(leftArr) and rightIndex < len(rightArr):
            if rightArr[rightIndex] < leftArr[leftIndex]:
                arr[mainIndex] = rightArr[rightIndex]
                rightIndex += 1
            else:
                arr[mainIndex] = leftArr[leftIndex]
                leftIndex += 1
            mainIndex += 1

        while leftIndex < len(leftArr):
            arr[mainIndex] = leftArr[leftIndex]
            leftIndex += 1
            mainIndex += 1
        
        while rightIndex < len(rightArr):
            arr[mainIndex] = rightArr[rightIndex]
            rightIndex += 1
            mainIndex += 1


#  outside function

myarr = [11, 9, 6, 8, 2, 5]

print(myarr)

shortMyArry(myarr)

print(myarr)