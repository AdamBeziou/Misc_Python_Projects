
print("English to Pig Latin Translator\n-------------------------------")
while True:
	print("\nType nothing and press ENTER to quit.")
	word_input = input("Type a word:").upper()
	if word_input != '':
		word = []
		con_seg = []
		
		i = len(word_input)

		for num in range(0,i):
			word.append(word_input[num])
	
		print(word)

		for num in range(0,i):
			if word[num] in ('A','E','I','O','U'):
				word = word[num:i]
				break
			else:
				con_seg.append(word[num])

		con_seg.append('AY')
		word = word + con_seg
		print(''.join(word))
		
		del word[:]
		del con_seg[:]
	
	else:
		break






	
