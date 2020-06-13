#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    max_jump = max(height)
    if (k < max_jump):
        return max_jump - k
    return 0


nk = input().split()
n = int(nk[0])
k = int(nk[1])
height = list(map(int, input().rstrip().split()))

result = hurdleRace(k, height)

print(str(result) + '\n')


