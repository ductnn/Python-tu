#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    result = 1
    while(n != 1):
        result *= n
        n -= 1
    print(result)


n = int(input())
extraLongFactorials(n)
