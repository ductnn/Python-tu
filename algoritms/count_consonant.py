# Count the number of consonant

vowels = 'aeiou'

input_srt_1 = 'ksdja ue'
input_srt_2 = 'ductnPrograming'

# Iterative
def iterative_count_consonant(input_srt):
	count = 0
	for i in range(len(input_srt)):
		if input_srt[i].lower() not in vowels and input_srt[i].isalpha():
			count += 1
	return count

# Recursive 
def recursive_count_consonant(input_srt):
	if input_srt == '':
		return 0
	if input_srt[0].lower() not in vowels and input_srt[0].isalpha():
		return 1 + recursive_count_consonant(input_srt[1:])
	else:
		return recursive_count_consonant(input_srt[1:])

print(iterative_count_consonant(input_srt_1))
print(iterative_count_consonant(input_srt_2))
print(iterative_count_consonant(vowels))

print('---------------------------------------')

print(recursive_count_consonant(input_srt_1))
print(recursive_count_consonant(input_srt_2))
print(recursive_count_consonant(vowels))
