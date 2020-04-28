# Find uppercase charater

input_str_1 = "ductnProgramming"
input_str_2 = "DuctnProgramming"
input_str_3 = "ductnprogramming"

# Iterative
def find_uppercase_iterative(input_str):
	for i in range(len(input_str)):
		if input_str[i].isupper():
			return True
	return False

# Recursive
def find_uppercase_recursive(input_str, idx=0):
	if input_str[idx].isupper():
		return True
	if idx == len(input_str) - 1:
		return False
	return find_uppercase_recursive(input_str, idx+1)
	
# Iterative
print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))

print('-----------------------------------------')

# Recursive
print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))
