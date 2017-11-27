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

def print_trainers(trainers):
	print "{:2}#  | {:<8}FN {:<13.13}LN | {:2}A | {:2}AB".format("","","","","","")
	for i in range(0, len(trainers)):
		print "{no:3}. | {tfn:10} {tln:15.15} | {age:3} | {tab:3} | {pri:8}".format(no = i+1,
																							tfn = trainers[i].first_name,
																							tln = trainers[i].last_name,
																							age = trainers[i].age,
																							tab = trainers[i].ability,
																							pri = trainers[i].market_value)

def run_buy_trainer(season):
	
	trainers_for_hiring = get_random_trainers(random.randint(1,10))
	
	print ""
	print "Your current trainer is: "
	season.manager.team.trainer.print_trainer()
	print ""
	print "Your currently available funds are: " + str(season.manager.team.finances.cash)
	print ""
	print "Trainers available for hiring: "
	print_trainers(trainers_for_hiring)
	print ""
	print "In case you would like to hire one of the trainers, please input the related ID"
	user_input = raw_input("Press Enter to return to Main Menu...")

	try:
		user_input = int(user_input)
		user_input -= 1

		if user_input in range (0,len(trainers_for_hiring)):
			print "You are selling your old trainer for EURO " + str(season.manager.team.trainer.market_value) + "."
			print "You are buying your new trainer for EURO " + str(trainers_for_hiring[user_input].market_value) + "."
			season.manager.team.finances.transaction(trainers_for_hiring[user_input].market_value, season.manager.team.trainer.market_value,season.year)
			season.manager.team.trainer = trainers_for_hiring[user_input]

		else:
			print "Invalid input ID"
			run_buy_trainer(season)

	except ValueError:
		menues.run_mainmenu(season)
