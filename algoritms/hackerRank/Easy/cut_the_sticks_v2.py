#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(sticks):
    count = 0
    if sticks:
        small_stick = min(sticks)
    else:
        return
    new_sticks = []
    for element in sticks:
        count = count + 1
        new_element = element - small_stick
        if new_element != 0:
            new_sticks.append(new_element)
    print(count) 
    cutTheSticks(new_sticks)


n = int(input())
arr = list(map(int, input().rstrip().split()))

result = cutTheSticks(arr)

print('\n'.join(map(str, result)))
print('\n')


