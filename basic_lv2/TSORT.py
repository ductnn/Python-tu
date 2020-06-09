n = int(input())
array = []

for i in range(n):
    t = int(input())
    array.append(t)

array.sort()
for i in array:
    print(i)
