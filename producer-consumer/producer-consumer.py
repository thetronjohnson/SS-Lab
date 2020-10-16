N = int(input("Enter the size of the buffer: "))

BUFFER  = []
MUTEX = 1


def wait(s):
	try:
		while(s<0):
			pass
		s-=1
		return(s)
	except:
		print("Argument must be an integer")

def signal(s):
	try:
		s+=1
		return(s)
	except:
		print("Argument must be an integer")

def producer(n):
	global BUFFER, MUTEX
	MUTEX = wait(MUTEX)
	BUFFER += [n]
	MUTEX = signal(MUTEX)
	print(f"Process {n} added to Buffer")

def consumer(n):
	global BUFFER,MUTEX
	MUTEX = wait(MUTEX)
	value = BUFFER.pop(BUFFER.index(n))
	MUTEX = signal(MUTEX)
	print(f"Process {n} removed from Buffer")

i=0
j=0
def main():
	global i,j
	command = int(input("\n1.Produce\n2.Consume\n3.Exit:\n=>"))
	if(command==1):
		if(MUTEX==1 and len(BUFFER)!=N):
			i+=1
			producer(i)
		else:
			print("Buffer is full\n")
	elif(command==2):
		if(MUTEX==1 and len(BUFFER)!=0):
			j+=1
			consumer(j)
		else:
			print("Buffer is empty\n")

	else:
		exit()


while(1):
	main()



