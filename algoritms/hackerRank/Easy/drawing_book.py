import os
import sys

n = int(input())
p = int(input())

print(min(p//2, n//2 - p//2))