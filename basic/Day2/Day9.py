n = int(input())

def Factorial(n):
	while (n>0):
		if(n==1):
			return 1
        else:
        	return n*Factorial(n-1)

print(Factorial(n))