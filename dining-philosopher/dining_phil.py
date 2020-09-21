import threading
import time
import random

class Philosopher(threading.Thread):
	running = True

	def __init__(self,index,left,right):
		threading.Thread.__init__(self)
		self.index = index
		self.left = left
		self.right = right

	def run(self):
		while (self.running):
			time.sleep(10)
			print(f"Philosopher {self.index} is hungry")
			self.dine()

	def dine(self):
		lft, rgt = self.left, self.right
		while self.running:
			lft.acquire()
			locked = rgt.acquire(False)
			if locked: break
			lft.release()

		else:
			return
		self.dining()
		lft.release()
		rgt.release()

	def dining(self):
		print(f"Philosopher {self.index} starts eating")
		time.sleep(10)
		print(f"Philosopher {self.index} finishes eating and starts thinking")

def main():
	N = int(input("Enter the number of Philosophers: "))
	forks = [threading.Semaphore() for i in range(N)]
	philosophers = [Philosopher(i,forks[i%N],forks[(i+1)%N]) for i in range(N)]
	Philosopher.running = True
	for p in philosophers: p.start()
	time.sleep(30)
	Philosopher.running = False
	print("Finish!")


if __name__ == '__main__':
	main()