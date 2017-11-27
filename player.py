#~ from __future__ import division
import random
import season
import menues

class Player:

	def __init__(self, team_category):
		self.first_name = self.set_first_name()
		self.last_name = self.set_last_name()
		self.age = random.randint(18,38)
		self.team = ""
		self.position = ""
		self.offense = team_category + random.randint(0,30)
		self.defense = team_category + random.randint(0,30)
		self.agression = random.randint(0,100)
		self.power = team_category + random.randint(0,30)
		self.endurance = team_category + random.randint(0,30)
		self.strength = self.get_strength()
		self.market_value = self.get_market_value()
		self.salary = self.get_salary()
		self.shot_goals = 0
		self.help_p = 0

	def get_strength(self):
		strength = self.offense + self.defense + self.power + self.endurance
		strength = strength / 4
		return strength

	def get_market_value(self):
		market_value = self.strength * 500
		return market_value

	def get_salary(self):
		salary = self.strength * 5
		return salary

	def set_first_name(self):
		List = open("player/first_names.txt",'r').read().splitlines()
		return random.choice(List)

	def set_last_name(self):
		List = open("player/last_names.txt",'r').read().splitlines()
		return random.choice(List)

def run_sell_player(season_1):
	
	print ""
	print "Your current team: "
	season_1.manager.team.print_players()
	print ""
	print "Your currently available funds are: " + str(season_1.manager.team.finances.cash)
	print ""
	if len(season_1.manager.team.players) < 12:
		print "You cannot sell any players, as you need a minimum of 11 players."
		user_input = raw_input("Press Enter to return to Main Menu...")
	
	elif len(season_1.manager.team.players) <= 12:
		print "Which player would you like to sell? Please input the related ID"
		user_input = raw_input("Press Enter to return to Main Menu...")

	try:
		user_input = int(user_input)
		user_input -= 1

		if user_input in range (0,len(season_1.manager.team.players)):
			print "You sold your player " + season_1.manager.team.players[user_input] + " at a prize of " + str(season_1.manager.team.trainer.market_value) + "."
			season_1.manager.team.finances.transaction(0,season.manager.team.players[user_input],season_1.year)
			season_1.manager.team.players.pop(user_input)

		else:
			print "Invalid input ID"
			run_sell_player(season_1)

	except ValueError:
		menues.run_mainmenu(season_1)
