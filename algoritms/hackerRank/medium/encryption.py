#!/bin/python3

import math
import os

# complete the encryption function below.
def encryption(s):
    L = len(s)
    rows = int(math.floor(L**(0.5)))
    columns = int(math.ceil(L**(0.5)))
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
