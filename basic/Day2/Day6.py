N = int(input())

for i in range(0, N):
	s = str(input())
	for j in range(0, len(s)):
		if j%2 == 0:
			print(s[j], end="")

	print(" ", end="")

	for j in range(0, len(s)):
		if j%2 != 0:
			print(s[j], end="")

	print("")