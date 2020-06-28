#!/bin/python3

import math
import os
import sys

# complete the encryption function below.
def encryption(s):
    L = len(s)
    rows = int(math.floor(math.sqrt(L)))
    columns = int(math.ceil(math.sqrt(L)))
    output = ""
    for i in range(columns):
        k = i
        for j in range(k,L,columns):
            output+=s[j]
        output+=" "
    return output



s = input()
result = encryption(s)
print(result + '\n')
