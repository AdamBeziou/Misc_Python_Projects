string_letters = []

print("Reverso\n-------")
string_input = input("Type anything: ")
i = len(string_input)

for num in range(0,i):
	string_letters.append(string_input[(i-1)-num])

print("".join(string_letters))
