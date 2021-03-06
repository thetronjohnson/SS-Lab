import matplotlib.pyplot as plt
from math import ceil

def roundup(x):
	return ceil(x/100.0)*100
class Scheduler:
	def __init__(self,name):
		self.name = name
		self.head = None
		self.requests = []
	def __repr__(self):
		return(str(self.name))

def seek(requests,head):
	time = 0
	served = []
	start = requests.index(head)
	for i in range(start,len(requests)-1):
		st = abs((requests[i+1]-requests[i]))
		print(f"From {requests[i]} to {requests[i+1]}, seektime:{st}")
		served += [requests[i]]
		time += st
	remaining = [i for i in requests if i not in served]
	remaining.sort(reverse=True)
	for i in range(len(remaining)-1):
		st = abs((remaining[i+1]-remaining[i]))
		print(f"From {remaining[i]} to {remaining[i+1]}, seektime:{st}")
		served += [remaining[i]]
		time += st
	served.append(remaining[-1])
	return ((f" Seektime: {time}\n Average Time: {time/len(requests)}"),served)

def plot(requestaxis,timeaxis,time):
	plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
	plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
	fig, ax = plt.subplots()
	ax.xaxis.set_label_position('top')
	ax.tick_params(labelbottom=False,labeltop=True)
	ax.plot(requestaxis,timeaxis)
	ax.set_title('SCAN Disk Scheduling')
	ax.invert_yaxis()
	plt.xlabel("Disk block")
	plt.ylabel("Time")
	plt.show()

scheduler = Scheduler("SCAN")
print("Enter the order of requests separated by comma:")
scheduler.requests += map(int,input().split(','))
scheduler.head = int(input("Current position of head: "))
timeaxis = [i for i in range(len(scheduler.requests)+1)]
requestaxis = [scheduler.head] + scheduler.requests
requestaxis.sort()
requestaxis.append(roundup(requestaxis[-1])-1)
time,served = seek(requestaxis,scheduler.head)
print(time)
#plot(served,timeaxis,time)