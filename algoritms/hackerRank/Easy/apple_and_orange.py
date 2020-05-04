#!/bin/python3

import math
import os
import random
import re 
import sys 

def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_1 = 0
    count_2 = 0

    for i in range(len(apples)):
        temp = a + apples[i]
        if (temp in range(s, t+1)):
            count_1 += 1
    
    for i in range(len(oranges)):
        temp = b + oranges[i]
        if (temp in range(s, t+1)):
            count_2 += 1
    
    print(count_1)
    print(count_2)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

