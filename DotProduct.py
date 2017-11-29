#2 vector dot product calculator

def V2DotProduct(vm):
	
	dot = 0
	numberv = len(vm)//3
	if numberv > 2:
		raise ValueError
	for i in range(0,numberv):
		dot += vm[i]*vm[i+numberv]
	print(dot)
	
vm = [1,2,3,3,2,1]
V2DotProduct(vm)
