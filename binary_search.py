def binarySearch(arr,min,max,value):
    if min <= max and max >= 0:
        mid = (min+max)//2

        if arr[mid] == value:
            print('Value is available at A[' + str(mid) + ']')
        elif value < arr[mid]:
            binarySearch(arr,min,mid-1,value)
        elif value > arr[mid]:
            binarySearch(arr,mid+1,max,value)
    else:
        print('Given Value: '+ str(value) + ' is not available')

myArr = [4,5,6,7,8,9,10]

print(myArr)
search = int(input('Enter Value to search: '))

binarySearch(myArr,0,len(myArr)-1,search)

