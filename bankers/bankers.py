
def needmatrix(need,maximum,allocated):
	for i in range(len(processes)):
		for j in range(R):
			need[i][j] = maximum[i][j] - allocated[i][j]


def safestate(processes,available,maximum,allocated):
	need = [[0 for j in range(R)] for i in range(len(processes))]
	needmatrix(need,maximum,allocated)
	finish = [0 for i in range(len(processes))]
	s_sequence = [0 for i in range(len(processes))]
	work = [i for i in available]

	count = 0
	while(count<len(processes)):
		found = False
		for p in range(len(processes)):
			if(finish[p]==0):
				executing = True
				for j in range(R):
					if(need[p][j]>work[j]):
						executing = False
						break
				if(j==R-1 and executing):
					for k in range(R):
						work[k] += allocated[p][k]
					s_sequence[count] = p
					count +=1
					finish[p] =1
					found = True

		if(found==False):
			print("System is not is safestate\n")
			return False
			exit()
	print("System is in safe state\n")
	print(f"safe Sequence: {s_sequence}")




P = int(input("Give number of processes:"))
R = int(input("Give number of resources: "))
processes = [i for i in range(P)]
max_r = [int(i) for i in input("Give the maximum available for each resources ->").split()]

print("\nGive the already allocated resources for each process")
allocated = [[int(i) for i in input(f"Process {j} ").split()] for j in range(P)]

print("\nGive the maximum resources for each process")
maximum = [[int(i) for i in input(f"Process {j}: ").split()] for j in range(P)]
tallocated = [0] * R
for i in range(P):
    for j in range(R):
        tallocated[j] += allocated[i][j]
print(f"\ntotal allocated resources : {tallocated}")
available = [max_r[i] - tallocated[i] for i in range(R)]
for num in available: 
    if num < 0:
        print("The allocation is more than the given number of resources")
        exit(0)
print(f"total available resources : {available}\n")
safestate(processes,available,maximum,allocated)

