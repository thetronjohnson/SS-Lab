
class Block:
	def __init__(self,value,nxt):
		self.value = value
		self.nxt = nxt
		self.table = []
	def blockindex(self,n):
		self.table.append(n)	

	def __repr__(self):
		return(f"{self.value}")

size = int(input('Enter the size of the storage: '))
array = [Block(0,None) for i in range(size)]


def main():
	global array
	global size
	global index_array
	idx, no = map(int,input("Enter index block number and the number of files on the index: ").split())
	if(array[idx].value==0):
		array[idx] = Block(idx,None)
	else:
		print("Index is already used\n")
		return
	count = 0
	i = 0
	while(count!=no):
		if(array[i].value == 0):
			array[i].value = 1
			res = [j for j,val in enumerate(array) if val.value==0]
			array[i].nxt = res[0]
			array[idx].blockindex(i)
			i = res[0]
			count +=1
		else:
			print("Location is already allocated")
			res = [j for j,val in enumerate(array) if val.value==0]
			i = res[0]

	print(f"Index: {idx}\n Index Table: {array[idx].table}")

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
