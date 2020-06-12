import math
import sys 

def getMoneySpent(keyboards, drives, b):
    n = len(keyboards)
    m = len(drives)
    res = []

    if min(keyboards) + min(drives) > b:
        result = -1
    else:
        for i in range(n):
            for j in range(m):
                cost = keyboards[i] + drives[j]
                if cost <= b:
                    res.append(cost)
        result = max(res)
    
    return result
    
bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

moneySpent = getMoneySpent(keyboards, drives, b)

print(str(moneySpent) + '\n')