#!/bin/python3

import math
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=valley=0
    for i in range(n):
        if(s[i]=='U'):
            level+=1
            if(level==0):
                valley+=1
        else:
            level-=1
    
    return valley

n = int(input().strip())
s = input().strip()

result = countingValleys(n, s)

print(str(result) + '\n')
