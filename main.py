import os, time, userinput, json

# Colors
red    = '\033[31m'
reverse='\033[07m'
yellow = '\033[93m'
white = '\033[0m'
green  = '\033[32m'
teal  = '\033[96m'
italic   = '\033[3m'
white2 = "\033[0;97m"

# Lists
entries = [] # Keeps track of entries

# Player variables
class Player():
	def __init__(self, name, happiness, gender, day):
		self.name = name
		self.happiness = happiness
		self.gender = gender
		self.day = day


def clear():
	os.system("clear")

def save(rlist):
  with open("variables.json", "w") as f:
    f.write(json.dumps(rlist))

def restore():
	f = open("variables.json", "r")
	rlist =	json.load(f)
	return rlist

# make an entry
def makeentry():
	f = open(data_directory + "/" +
					 entryname + ".txt", "w+")
	entries.append(entryname)
	save(entries)
	f.write(str(month) + "-" + str(day) + "-" + str(year) + "\n\n")
	f.write(text)
	f.close()

def createentry():
	global entryname
	global month
	global day
	global year
	global text

	entryname = input("Name of entry\n> ")
	clear()
	while True:
		try:
			month = int(input("What is the month\n> "))
			break
		except:
			print("invalid option")
			time.sleep(2)
			clear()
			pass
	clear()
	while True:
		try:
			day = int(input("What is the day\n> "))
			break
		except:
			print("invalid option")
			time.sleep(2)
			clear()
			pass
	clear()	
	while True:
		try:
			year = int(input("What is the year\n> "))
			break
		except:
			print("invalid option")
			time.sleep(2)
			clear()
			pass
	clear()
	text = input("Your text\n> ")
	makeentry()
	clear()

# display 
def display():
	while True:
		print(teal + "Name: " + white + p.name)
		#print(teal + "Happiness: " + white + str(p.happiness[0]))
		print(teal + "Gender: " + white + p.gender)
		print("")
		cmdlist = ["Create or Edit Entry", "View Entries", "Quit"]
		cmd = userinput.input_list("Commands:", cmdlist)
		if cmd == "Create or Edit Entry":
			clear()
			print("If you want to create a new entry, make sure that your entry name is unique. If you want to edit an entry, type the name of the entry you want to edit when it prompts you with 'name of entry'.")
			createentry()
		elif cmd == "View Entries":
			clear()
			view = userinput.input_list("Which Entry do you want to view?", entries)
			if view in entries:
				f = open(data_directory + "/" + view + ".txt", "r")
				clear()
				print(f.read())
				input("")
				clear()
		elif cmd == "Quit":
			clear()
			print(red + "exited, terminated.")
			break
		


data_directory = "journal"
os.system("mkdir -p " + data_directory)

# main inputs
name = input("Enter your name\n> ")
clear()
gender = input("Enter your gender\n> ")
clear()
p = Player(name, 1, gender, 1)

entries = restore()
# call display
display()
save(entries)


