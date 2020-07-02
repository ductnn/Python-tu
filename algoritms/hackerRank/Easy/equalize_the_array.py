#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    count=0
    G={}
    for i in arr:
        if i not in G:
            for j in arr:
                if i==j:
                    count=count+1
            G[i]=count
            count=0
            
    max_val=max(G, key=G.get)
    return (len(arr)-G[max_val])


n = int(input())
arr = list(map(int, input().rstrip().split()))
result = equalizeArray(arr)

print(str(result) + '\n')

