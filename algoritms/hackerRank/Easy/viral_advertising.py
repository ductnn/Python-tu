#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared =5
    cumulative=0
    for i in range(1,n+1):
        liked = shared//2
        cumulative+=liked
        shared = liked*3
    return cumulative


n = int(input())

result = viralAdvertising(n)

print(str(result) + '\n')

