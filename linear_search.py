# Linear Search

def search(arr, value):

    for i in range(0,len(arr)):
        if value == arr[i]:
            print('Value is found at A[' + str(i) +']')
            return
        
    print('Given Value: '+ str(value) + ' is not found')

myarr = [2,5,1,7,3,9]

print(myarr)
value = int(input('Enter value to search: '))
search(myarr,value)