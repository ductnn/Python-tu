#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    boolean = False
    count=0
    for i in range(n+1):
        if(boolean == False):
            count+=1
            boolean = True
        else:
            count*=2
            boolean=False
    return count


t = int(input())
for t_itr in range(t):
    n = int(input())
    result = utopianTree(n)
    print(str(result) + '\n')

