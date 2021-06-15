#Selection short
values = [23,4,8,3,5,1]
minimum = 0
for i in range(len(values)):
    minimum = i
    for j in range(i+1,len(values)):
        if values[j] < values[minimum]:
            minimum = j 
    
    temp = values[i]
    values[i] = values[minimum]
    values[minimum] = temp

print(values)
