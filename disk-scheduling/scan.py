import matplotlib.pyplot as plt

class Scheduler:
	def __init__(self,name):
		self.name = name
		self.head = None
		self.requests = []
	def __repr__(self):
		return(str(self.name))

def seek(requests,served,head):
	time = 0
	start = requests.index(head)
	for i in range(start,len(requests)-1):
		st = abs((requests[i+1]-requests[i]))
		print(f"From {requests[i]} to {requests[i+1]}, seektime:{st}")
		#served.append(requests.pop(i))
		time += st
	return (f" Seektime: {time}\n Average Time: {time/len(requests)}")


scheduler = Scheduler("SCAN")
print("Enter the order of requests separated by comma:")
scheduler.requests += map(int,input().split(','))
scheduler.head = int(input("Current position of head: "))
timeaxis = [i for i in range(len(scheduler.requests)+1)]
requestaxis = [scheduler.head] + scheduler.requests
served = []
requestaxis.sort()
time = seek(requestaxis,served,scheduler.head)
print(time)