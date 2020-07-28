#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    total = 0
    count = 0
    array = [0] * (n+1)

    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]

        array[a] += k
        array[b] -= k

        # for i in range(a, b):
        #     array[i] += k

    for i in array:
        count = count + i
        if count > total:
            total = count
    
    return total

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')


