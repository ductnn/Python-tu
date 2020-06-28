amt, total = input().split()
amt = int(amt)
total = float(total)

if(amt % 5==0):
    if(total - amt - 0.50 >= 0):
        total = total - amt - 0.50

print(total)
