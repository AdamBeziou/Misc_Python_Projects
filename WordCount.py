def WordCount(string):
	string_l = string.split(' ')
	return len(string_l)
	
def WordCountText(doc):
	string_l = open(doc).read().split(' ')
	return len(string_l)

v = WordCount("1 2 3 4 5 !!! !")
print(v)
v = WordCountText("Test.txt")
print(v)