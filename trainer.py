import random

class Trainer:

	def __init__(self):
		self.first_name = self.set_first_name()
		self.last_name = self.set_last_name()
		self.age = random.randint(40,70)
		self.ability = random.randint(0,100)
		self.team = ""

	def set_first_name(self):
		List = open("player/first_names.txt",'r').read().splitlines()
		return random.choice(List)

	def set_last_name(self):
		List = open("player/last_names.txt",'r').read().splitlines()
		return random.choice(List)
	
	def print_trainer(self):
		print("Trainer: " + self.first_name + " " + self.last_name + " - Faehigkeit: " + str(self.ability))

