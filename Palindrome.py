def CheckPalindrome(word):
	p_join = ''
	palindrome = []
	for i in range(0,len(word)):
		palindrome.append(word[len(word) - 1 - i])
	if p_join.join(palindrome) == word:
		return True
	else:
		return False
		
word = "racecar"
v = CheckPalindrome(word)
print(v)