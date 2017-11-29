print("Binary Convertor (Little-endian)\n------------------------")
binary = input("Enter a binary integer: ")
binar_l = len(binary)
dec = 0

print(binary)
print(binar_l)

for i in range(0, binar_l):
	dec += (int(binary[i])*(2**i))
	print(dec)
print(dec)
