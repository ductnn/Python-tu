N = int(input())
phone_book = {}

for i in range(N):
	a = str(input()).split(" ")
	name = a[0]
	phone = int(a[1])
	phone_book[name] = phone

# for j in range(N):
while True:
	try:
		name = str(input())
		if name in phone_book:
			phone = phone_book[name]
			print(name + "=" + str(phone))
		else:
			print("Not found")
	except EOFError:
		break