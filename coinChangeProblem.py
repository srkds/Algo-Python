# make a coin change problem using dynamic programming
import numpy as np
import copy as cp

coins = [1,5,6,8]
total = 11
# coins = [1,2,5]
# total = 11
selectedCoins = []

t = np.zeros((len(coins),total+1))

for i in range(0,len(coins)):
    for j in range(0,total+1):

        if j == 0:
            t[i][j] = 0
        if coins[i] == 1:
            t[i][j] = j
        elif j >= coins[i]:
            temp = (t[i-1][j],1+t[i][j-coins[i]])
            # print(temp)
            t[i][j] = min(temp)
        else:
            t[i][j] = t[i-1][j]

print(t)

r = len(coins)-1
c = total
while c > 0 and r > -1:
    if r == 0 and c != 0:
        selectedCoins.append(coins[r])
        c -= coins[r] 
    else:
        curVal = t[r][c]
        ubvVal = t[r-1][c]
        if curVal == ubvVal:
            r = r-1
        else:
            selectedCoins.append(coins[r])
            c -= coins[r] 
print("Minimum Num of Coins are : ", t[i][j])
print("List of Coins : ",selectedCoins)