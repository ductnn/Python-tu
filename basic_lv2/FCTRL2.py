n = int(input())

def Factotial(n):
    while (n>0):
        if (n == 1):
            return 1
        else: return n*Factotial(n-1)

for i in range(n):
    a = int(input())
    print(Factotial(a))
