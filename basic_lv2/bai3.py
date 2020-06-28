n, k = map(int,input().split(" "))
count = 0

for i in range(1, n):
    q = int(input())
    if(q%k == 0):
        count+= 1

print(count)
