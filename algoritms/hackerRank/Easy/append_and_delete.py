#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # Case A (i) 
    if ((len(s) + len(t)) < k): 
        return 'Yes'
  
    # finding common length of both string 
    commonLength = 0
    for i in range(0, min(len(s),  
                          len(t)), 1): 
        if (s[i] == t[i]): 
            commonLength += 1
        else: 
            break
  
    # Case A (ii)- 
    if ((k - len(s) - len(t) + 2 * 
                commonLength) % 2 == 0): 
        return 'Yes'
  
    # Case B- 
    return 'No'



s = input()
t = input()
k = int(input())

result = appendAndDelete(s, t, k)

print(result + '\n')

