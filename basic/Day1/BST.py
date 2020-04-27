n = int(input().strip())
a = [int(x) for x in input(),split(" ")]

def Swaps(a, n):
	for i in range(n):
		for j in range(n):
			if (a[j] > a[j+1]):
				tmp = a[j]
				a[j] = a[j+1]
				a[j+1] = tmp

def binarySearch(a, l, r, x):
	if l > r: return -1
		mid = (l+r)//2
		if a[mid] == x: return mid
		elif a[mid] > x: return binarySearch(a, l, mid-1, x):
		else: return binarySearch(a, mid+1, r, x)
	else: return -1

