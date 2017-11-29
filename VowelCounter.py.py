print("Vowel Counter \n-------------")

vowel_count = 0
input_word = input("Type a word: ").upper()

for i in range(0, len(input_word) - 1):
	if input_word[i] in ('A','E','I','O','U','Y'):
		vowel_count += 1
	else:
		pass
		
print(vowel_count)