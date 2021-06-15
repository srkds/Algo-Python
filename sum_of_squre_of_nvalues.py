# Sum of squre of n numbers

doSumOf = [2,5,3,1,2]

print('Values:' + str(doSumOf))

sumOfSqure = 0
for i in doSumOf:
    sumOfSqure = (i*i)+sumOfSqure

print("Sum Of All values Of Squres is: " + str(sumOfSqure))