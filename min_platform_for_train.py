# this programm finds minimum no of platform needed for train


def findMinPlatform(arr,dep,n):



    platform_needed = 1
    result = 1
    i = 1
    j = 0

    while i < n and j < n:
        
        if arr[i] < dep[j]:
            platform_needed += 1
            i += 1
        elif arr[i] > dep[j]:
            platform_needed -= 1
            j += 1
        
        if platform_needed > result:
            result = platform_needed
    
    return result


arr = [200,210,300,320,350,500]
dep = [230,320,340,400,430,520]

print(findMinPlatform(arr,dep,len(arr)))