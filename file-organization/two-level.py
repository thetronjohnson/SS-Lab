from termcolor import colored

class Directory:
	def __init__(self,name):
		self.name = name
		self.files = []
		self.folders = {}
	def createfile(self,file):
		if(file not in self.files):
			self.files.append(file)
			print(f"File {file} has been created inside the directory {self.name}")
		else:
			print(f"File {file} is already present in the directory")

	def createfolder(self,folder):
		if(folder not in self.folders):
			self.folders[folder.name] = folder
			print(f"Folder {folder.name} has been created inside the directory {self.name}")
		else:
			print(f"Folder{folder.name} is already present in the directory")

	def remove(self,query):
		if(query in self.files):
			self.files.remove(query)
			print(f"{query} has been removed from the directory {self.name}")
		elif(query in self.folders):
			self.folders.pop(query)
			print(f"{query} has been removed from the directory {self.name}")
		else:
			print("No such file exists")
	def search(self,query):
		if(query in self.files):
			print(f"{query} is present inside the directory {self.name}")
		elif(query in self.folders):
			print(f"{query} is present inside the directory {self.name}")
		else:
			print(f"{query} is not present in this directory")

	def __repr__(self):
		return(f"Directory name: {self.name}")

OPTIONS = {
	'create folder':6,
	'create file':1,
	'remove':2,
	'search':3,
	'display':4,
	'exit':5,
	'open folder':7,
	'insert into':8,
	'remove from':9
}


	

def driver(directory,OPTIONS,option):
	if(OPTIONS[option]==6):
		foldername = input("Enter directory name: ")
		folder = Directory(foldername)
		directory.createfolder(folder)
	elif(OPTIONS[option]==1):
		filename = input("Enter file name: ")
		directory.createfile(filename)
	elif(OPTIONS[option]==2):
		filename = input("Enter file/directory name: ")
		directory.remove(filename)
	elif(OPTIONS[option]==3):
		filename = input("Enter file/directory name: ")
		directory.search(filename)
	elif(OPTIONS[option]==4):
		print(f"Directory : {directory.name}")
		for folder in directory.folders:
			print(colored(f"{folder} ","green"),end="")
		for file in directory.files:
			print(colored(f"{file} ","blue") ,end="")
		print()
	elif(OPTIONS[option]==9):
		foldername = input("Enter directory name: ")
		filename = input("Enter filename: ")
		directory.folders[foldername].remove(filename)
	elif(OPTIONS[option]==7):
		foldername = input("Enter foldername to open: ")
		if(foldername in directory.folders):
			require_folder = directory.folders[foldername]
			print(colored(f"Location: {directory.name}/{foldername}","red"))
			for name in require_folder.files:
				print(colored(f"{name} ","blue"),end="")

	elif(OPTIONS[option]==8):
		foldername = input("Enter foldername to add files: " )
		filename = input("Enter filename: ")
		directory.folders[foldername].createfile(filename)
	elif(OPTIONS[option]==5):
		print("Exiting...")
		exit(0)
	else:
		print("Invalid Input")
	



name = input("Enter the directory name: ")
directory  = Directory(name)
print(f"Directory {directory.name} has been created\n")
while(1):
	try:
		option = input("\nEnter Command: ")
		driver(directory,OPTIONS,option)
	except:
		print("Exiting Filesystem...")
		exit()