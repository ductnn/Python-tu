#!/bin/python3
import sys
import math


q = int(input().strip())
for a0 in range(q):
    a, b = map(int, input().strip().split(' '))
    lower_limit = math.ceil(math.sqrt(a))
    upper_limit = math.floor(math.sqrt(b))
    print(upper_limit - lower_limit + 1)