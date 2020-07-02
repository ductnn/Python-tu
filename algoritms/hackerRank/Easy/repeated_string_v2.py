#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    n1=(n//len(s))
    x=s.count('a')
    x1=n1*x
    x2=s[:n%(len(s))].count('a')
    return x1+x2

s = input()
n = int(input())
result = repeatedString(s, n)

print(str(result) + '\n')

