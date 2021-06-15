# Quick short 

def doPartition(arr,low,high):
    pivot = arr[high]

    i = low - 1

    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    
    temp = arr[high]
    arr[high] = arr[i+1]
    arr[i+1] = temp

    return i+1
    

def shortArray(arr,lowerBound,upperBound):
    if lowerBound < upperBound:
        loc = doPartition(arr,lowerBound,upperBound)
        shortArray(arr,lowerBound,loc-1)
        shortArray(arr,loc+1,upperBound)

myArry = [10,7,11,5,3,11,12,2,1,6,23,15,9]

print("Before Shorting: " + str(myArry))

shortArray(myArry,0,len(myArry)-1)

print("After Shorting: " + str(myArry))