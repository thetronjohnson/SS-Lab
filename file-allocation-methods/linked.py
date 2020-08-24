class Block:
	def __init__(self,value,nxt):
		self.value = value
		self.nxt = nxt


	def __repr__(self):
		return(str(self.value))


size = int(input('Enter the size of the storage: '))
array = [Block(0,None) for i in range(size)]

def main():
	global array
	global size
	st,l  = map(int,input("Enter starting address and length of block: ").split())
	count = 0
	i = st
	while(count!=l):
		if(array[i].value==0):
			array[i].value = 1
			res = [j for j,val in enumerate(array) if val.value==0]
			array[i].nxt = res[0]
			print(f"Location: {i} Value: {array[i].value}, Next:{array[i].nxt}")
			i = res[0]
			count +=1
		else:
			print(f"location {i} is already allocated")
			res = [j for j,val in enumerate(array) if val.value==0]
			i = res[0]

def driver():
	main()
	print(array)
	print()
	while(1):
		choice = input("Enter more files? (Y): ")
		if(choice=='Y' or choice=='y'):
			main()
			print(array)
			print()
		else:
			exit()

driver()




