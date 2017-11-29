import random

print("Roshambo\n--------")

while True:
	ch_comp = random.randint(1,4)
	print("1. Rock\n2. Paper\n3. Scissors\n")
	ch = input("#")
	try:
		ch_num = int(ch)
		if ch_comp == 1:
			print("Computer chose rock!")
			if ch_num == 2:
				print("You win!")
			else:
				print("You lose!")
		elif ch_comp == 2:
			print("Computer chose paper!")
			if ch_num == 1:
				print("You win!")
			else:
				print("You lose!")
		else:
			if ch_num == 1:
				print("Computer chose scissors!")
				print("You win!")
			else:
				print("You lose!")
	except ValueError:
		print("Only enter a number.\n")