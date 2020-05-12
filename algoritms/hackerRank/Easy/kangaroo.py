import sys

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

def kangaroo(x1, v1, x2, v2):
    if v1 == v2 and x1 == x2:
        return 'YES'
    elif v1 == v2:
        return 'NO'
    
    x = (x2 - x1) / (v1 - v2)
    if(x == round(x) and x > 0):
        return 'YES'
    else:
        return 'NO'

resutl = kangaroo(x1, v1, x2, v2)
print(resutl)