import sys

def gcd(a, b):
    while a % b != 0:
        a, b = b, (a % b)
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

# get total
def getTotalX(a, b):
    lcm_num = a[0]
    gcd_num = b[0]

    if len(a) > 1:
        for x in range(1,len(a)):
            lcm_num =  (lcm_num * a[x])//gcd(lcm_num,a[x])
    if len(b) > 1:
        for x in range(1,len(b)):
            gcd_num = gcd(gcd_num,b[x])
    count = 0
    for x in range(lcm_num, gcd_num+1, lcm_num):
        if gcd(x, gcd_num) == x:
            count += 1
    return count

# main
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)