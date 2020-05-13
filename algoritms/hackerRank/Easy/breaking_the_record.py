import math
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxi = scores[0]
    mini = scores[0]
    maxCount = 0
    minCount = 0

    for i in range(len(scores)):
        if(scores[i] > maxi):
            maxi = scores[i]
            maxCount += 1
        if(scores[i] < mini):
            mini = scores[i]
            minCount += 1

    return [maxCount, minCount]

n = int(input().strip())
scores = list(map(int, input().strip().split(' ')))

result = breakingRecords(scores)

print(' '.join(map(str, result)))