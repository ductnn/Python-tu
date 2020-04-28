# Calculate the length of string

input_str = 'DuctnPrograming'

print(len(input_str))

# Iterative
def iterative_string_length(input_str):
	count = 0;
	for i in range(len(input_str)):
		count += 1
	return count

# Recursive
def recursive_string_length(input_str):
	if input_str == '':
		return 0
	return 1 + recursive_string_length(input_str[1:])

print('--------------------------')
print(iterative_string_length(input_str))
print('--------------------------')
print(recursive_string_length(input_str))