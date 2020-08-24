size = int(input('Enter the size of the storage: '))
array = [0 for i in range(size)]

def main():
	global array
	global size
	st, l = map(int,input("Enter the starting address and length of file: ").split())
	i = st
	while(i<(st+l)) :
		if(array[i]==0):
			array[i]=1
			i+=1
		else:
			print("Block has been already allotted try another series of blocks!")
			break

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