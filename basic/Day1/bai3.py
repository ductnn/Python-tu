#x = int(input())
#def fact(x):
#    if x == 0:
#        return 1
#    return x*(fact(x-1))
#print(fact(x))

a = [8, 5, 9]
def swap(a):
    for i in range(0, 3):
        tmp = int()
        if (a[i] > a[i+1]):
            a[i] = tmp
            tmp = a[i+1]
            a[i+1] = a[i]
print(swap(a))
