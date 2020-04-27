import sys

n = int(input().strip())
a = [int(x) for x in input().split(" ")]
numSwap = 0

for i in range(n):
	for j in range(n-1):
		if (a[j] > a[j+1]):
			tmp = a[j]
			a[j] = a[j+1]
			a[j+1] = tmp
			numSwap += 1

	if (numSwap == 0): break

print("Array is sorted in " + str(numSwap) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[len(a) - 1]))