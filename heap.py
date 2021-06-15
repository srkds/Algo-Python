def heapify(arr, length, currentLargeIndex):

    large = currentLargeIndex
    lch = 2*currentLargeIndex + 1
    rch = 2*currentLargeIndex + 2

    if lch < length and arr[lch] > arr[large]:
        large = lch
    
    if rch < length and arr[rch] > arr[large]:
        large = rch

    if large != currentLargeIndex:
        temp = arr[large]
        arr[large] = arr[currentLargeIndex]
        arr[currentLargeIndex] = temp

        heapify(arr,length,large)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)


myarr = [1,10,7,12,5,15,16,3]
print(myarr)
heapSort(myarr)
print(myarr)

