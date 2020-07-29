#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))

    d = d%n
    for i in range(d, n):
        print(a[i], end=" ")
    
    for j in range(d):
        print(a[j], end=" ")
