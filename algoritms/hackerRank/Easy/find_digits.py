#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    count = 0
    for i in list(str(n)):
        if int(i) != 0 and n % int(i) == 0:
            count += 1
    return count


t = int(input())

for t_itr in range(t):
    n = int(input())

    result = findDigits(n)

    print(str(result) + '\n')


