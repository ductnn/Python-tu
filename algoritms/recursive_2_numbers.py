x = 3
y = 5

# Recursive
def recursive_2nums(x, y):
    if x < y:
        return recursive_2nums(y, x)
    if y == 0:
        return 0
    return x + recursive_2nums(x, y - 1)

print(x * y)
print(recursive_2nums(x, y))
