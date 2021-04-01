from termcolor import colored
import time, os

# User Input using Dicts
def GetUserInput(greetmessage, input_menu):
	if greetmessage:
		print(greetmessage)
	for item, item_value in input_menu.items():
		print("[" + item + "] " + item_value)
	while True:
		user_input = input("> ")	
		if user_input in input_menu.keys():
			return input_menu[user_input]
		else:
			print(colored("Invalid Option.", "red"))

def input_list(greetmessage, input_menu_list):
	input_menu = {}
	index = 1
	for item in input_menu_list:
		input_menu[str(index)] = item
		index += 1
	if greetmessage:
		print(greetmessage)
	for index, item_value in input_menu.items():
		print("" + index + " " + item_value)
	while True:
		user_input = input("> ")	
		if user_input in input_menu.keys():
			return input_menu[user_input]
		else:
			print(colored("Invalid Option.", "red"))
			time.sleep(2)
			os.system("clear")