#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    count = 0

    for item in queries:
        if item == strings:
            count += 1
    
    return count

if __name__ == '__main__':
    strings_count = int(input())
    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    for _ in range(queries_count):
        queries_item = input()
        res = matchingStrings(queries_item, strings)

        print(res)
        # print('\n'.join(map(str, res)))
        # print('\n')
