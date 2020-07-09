import math
import os
import random
import re
import sys

def c():
    n,m = map(int,input().split())
    l = []
    mx = 0
    for _ in xrange(n):
        w = int('0b' + input(),2)
        l.append(w)

	cnt = 0

    for i in xrange(n):
        for j in xrange(i+1,n):
            p = bin(l[i]|l[j]).count('1')
            if p > mx:
                mx = p
                cnt = 1
            elif p == mx:
                cnt += 1
    return mx,cnt

a,b = c()
print(a)
print(b)