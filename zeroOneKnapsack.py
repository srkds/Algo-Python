import numpy as np
profit = [0,1,2,5,6]
weight = [0,2,3,4,5]

capacity = 8
objacts = 4

k = np.zeros((5,9))

# print(k)

for i in range(0,objacts+1):
    for w in range(0,capacity+1):
        if i == 0 or w == 0:
            k[i][w] = 0
        elif weight[i] <= w:
            temp = (profit[i]+k[i-1][w-weight[i]],k[i-1][w])
            k[i][w] = max(temp)
        else:
            k[i][w] = k[i-1][w]
    

r = objacts
c = capacity
while r >= 0 and c >0:
    if k[r][c] == k[r-1][c]:
        # print(r," = 0")
        r -= 1
    else:
        print("Selected Weight: ", weight[r], " Profit: ", profit[r])
        # print(r," = 1")
        c = c-weight[r]
        r -= 1

print("Max profit :",k[objacts][w])