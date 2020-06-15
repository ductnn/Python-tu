
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def reverse(n):
    ret = 0
    while(n):
        ret = ret*10 + n%10
        n = n//10
    return ret

def beautifulDays(i, j, k):
    count=0
    for l in range(i,j+1):
        n = reverse(l)
        if(abs(l-int(n))%k == 0):
            count+=1
    return count


ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])

result = beautifulDays(i, j, k)

print(str(result) + '\n')