#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    lastAnswer = 0
    seq = []

    for i in range(n):
        seq.append([])
    
    for query in queries:
        x = query[1]
        y = query[2]

        if query[0] == 1:
            index = ((x ^ lastAnswer) % n)
            seq[index].append(y)
        elif query[0] == 2:
            index = ((x ^ lastAnswer) % n)
            size = y % (len(seq[index]))
            lastAnswer = seq[index][size]
    
            return lastAnswer

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

        result = dynamicArray(n, queries)
    
        print(result)

    # print('\n'.join(map(str, result)))
    # print('\n')

