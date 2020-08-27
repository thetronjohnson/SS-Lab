from termcolor import colored

class Directory:
	def __init__(self,name):
		self.name = name
		self.files = []
	def create(self,file):
		if(file not in self.files):
			self.files.append(file)
			print(f"{file} has been created inside the directory {self.name}")
		else:
			print(f"{file} is already present in the directory")

	def remove(self,file):
		if(file in self.files):
			self.files.remove(file)
			print(f"{file} has been removed from the directory {self.name}")
		else:
			print("No such file exists")
	def search(self,file):
		if(file in self.files):
			print(f"{file} is present inside the directory {self.name}")
		else:
			print(f"{file} is not present in this directory")

	def __repr__(self):
		return(f"Directory name: {name}")

OPTIONS = {
	'create':1,
	'remove':2,
	'search':3,
	'display':4,
	'exit':5
}

def driver(directory,OPTIONS,option):
	try:
		if(OPTIONS[option]==1):
			filename = input("Enter filename: ")
			directory.create(filename)
		elif(OPTIONS[option]==2):
			filename = input("Enter filename: ")
			directory.remove(filename)
		elif(OPTIONS[option]==3):
			filename = input("Enter filename: ")
			directory.search(filename)
		elif(OPTIONS[option]==4):
			print(colored(f"Directory : {directory.name}","red"))
			for file in directory.files:
				print(colored(f"{file}  ","blue"),end="")
			print()
		elif(OPTIONS[option]==5):
			print("Exiting...")
			exit(0)
		else:
			print("Invalid Input")
	except:
		print("Invalid Input")


name = input("Enter the directory name: ")
directory  = Directory(name)
print((colored(f"Directory {directory.name} has been created\n","yellow")))
while(1):
	try:
		option = input("Enter Command: ")
		driver(directory,OPTIONS,option)
	except:
		print("Exiting Filesystem...")
		exit()