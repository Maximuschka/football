import random
import player
import menues

class Trainer:

	def __init__(self):
		self.first_name = self.set_first_name()
		self.last_name = self.set_last_name()
		self.age = random.randint(35,70)
		self.ability = random.randint(0,100)
		self.market_value = self.get_market_value()
		self.salary = self.get_salary()
		self.team = ""

	def set_first_name(self):
		List = open("player/first_names.txt",'r').read().splitlines()
		return random.choice(List)

	def set_last_name(self):
		List = open("player/last_names.txt",'r').read().splitlines()
		return random.choice(List)

	def get_market_value(self):
		market_value = self.ability * 500
		return market_value
		
	def get_salary(self):
		salary = self.ability * 10
		return salary

	def print_trainer(self):
		print("Trainer: " + self.first_name + " " + self.last_name + " - Faehigkeit: " + str(self.ability))

def get_random_trainers(n):

	trainers = []

	for i in range (0,n):
		dummy_trainer = Trainer()
		trainers.append(dummy_trainer)

	return trainers

def delete_random_trainers(trainers,n):
	
	"""
	n - amount of trainers to be deleted
	"""
	
	for i in range (0,n):
		del_id = random.randint(0,len(trainers)-1)
		trainers.pop(del_id)


def print_trainers(trainers):
	print "{:2}#  | {:<8}FN {:<13.13}LN | {:2}A | {:2}AB".format("","","","","","")
	for i in range(0, len(trainers)):
		print "{no:3}. | {tfn:10} {tln:15.15} | {age:3} | {tab:3} | {pri:8}".format(no = i+1,
																							tfn = trainers[i].first_name,
																							tln = trainers[i].last_name,
																							age = trainers[i].age,
																							tab = trainers[i].ability,
																							pri = trainers[i].market_value)


