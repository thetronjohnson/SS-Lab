import matplotlib.pyplot as plt

class Scheduler:
	def __init__(self,name):
		self.name = name
		self.head = None
		self.requests = []
	def __repr__(self):
		return(str(self.name))

def seektime(requests,head):
	time = abs(requests[0]-head)
	for i in range(len(requests)-1):
		time += abs((requests[i+1]-requests[i]))
	return (f" Seektime: {time}\n Average Time: {time/len(requests)}")

def plot(requestaxis,timeaxis,time):
	plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
	plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
	fig, ax = plt.subplots()
	ax.xaxis.set_label_position('top')
	ax.tick_params(labelbottom=False,labeltop=True)
	ax.plot(requestaxis,timeaxis)
	ax.set_title('FCFS Disk Scheduling')
	ax.invert_yaxis()
	plt.xlabel("Disk block")
	plt.ylabel("Time")
	plt.show()

scheduler = Scheduler("FCFS")
print("Enter the order of requests separated by comma:")
scheduler.requests += map(int,input().split(','))
scheduler.head = int(input("Current position of head: "))
timeaxis = [i for i in range(len(scheduler.requests)+1)]
requestaxis = [scheduler.head] + scheduler.requests
time = seektime(scheduler.requests,scheduler.head)
for i in range(len(requestaxis)-1):
	print(f"From {requestaxis[i]} to {requestaxis[i+1]}, seektime:{abs(requestaxis[i+1]-requestaxis[i])}")
print()
print(time)
plot(requestaxis,timeaxis,time)
