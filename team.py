#~ from __future__ import division
from operator import itemgetter, attrgetter, methodcaller
from random import randint
import player
import training
import trainer
import finances
import stadium
import operator
import menues

class Team:
	
	#~ counter = 0

	def __init__(self, name, wappen_image):
		#~ type(self).counter += 1
		self.category = randint(35,70)
		self.name = name
		self.wappen = wappen_image
		self.trainers = self.add_trainer()
		self.training_status = True
		self.trained_feature = 0
		self.tactic = randint(0,2)
		self.moral = 2
		self.games_played = 0
		self.points = 0
		self.scored_goals = 0
		self.received_goals = 0
		self.attempts = 0
		self.players = self.add_players()
		self.strength = self.get_strength()
		self.league = 1
		self.title = 0
		self.finances = finances.Finances(self)
		self.stadium = stadium.Stadium(self)
		self.guest_potential = 0
		self.home_md = False

#Team category - good (70) or bad (35) - influences player strength when initiating Players

	#~ def __del__(self):
		#~ type(self).counter -= 1


	def get_name(self):
		return self.name

	def get_efficiency(self):
		if (self.attempts > 0):
			eff = (self.scored_goals / self.attempts)*100
			return eff
		
		else:
			return 0

	def get_strength(self):

		active_players = self.players[0:11]

		strength = 0

		for i in range(0, len(self.players)):
			self.players[i].set_current_strength()

		for j in range(0, len(active_players)):
			strength += active_players[j].strength

		return strength/len(active_players)

	def get_diff_goals(self):
		diff_goals = self.scored_goals - self.received_goals
		return diff_goals

	def get_income_match_won(self):
		income = 1000 / self.league
		return income

	def get_income_match_draw(self):
		income = (1000 / self.league)/2
		return income

	def set_guest_potential(self):
		self.guest_potential = 40000 / (self.league*2)

	def set_training_status(self, status):
		self.training_status = status

	def set_trained_feature(self, feature):
		self.trained_feature = feature

	def set_current_strength(self):
		self.strength = self.get_strength() 

	def set_tactic_random(self):
		self.tactic = randint(0,2)
		
	#~ def set_positions(self):
		#~ self.players[0].position = 0
		#~ for i in range(1, 5):
			#~ self.players[i].position = 1
		#~ for i in range(5, 9):
			#~ self.players[i].position = 2
		#~ for i in range(9, len(self.players)):
			#~ self.players[i].position = 3

	def add_players(self):
		players = []
		for i in range(0,12):
			player1 = player.Player(self.category)
			player1.team = self.name
			players.append(player1)
		
		players[0].position = 0
		for i in range(1, 5):
			players[i].position = 1
		for i in range(5, 9):
			players[i].position = 2
		for i in range(9, len(players)):
			players[i].position = 3
		
		return players
	
	def add_trainer(self):
		trainers = []
		trainer1 = trainer.Trainer()
		trainers.append(trainer1)
		return trainers

	def print_players(self):
		print "Active players:"
		active_players = self.players[0:11]
		player.print_players_hl()
		player.print_players_data(active_players,0,len(active_players))
		if len(self.players) > 11:
			print ""
			print "Players in reserve:"
			player.print_players_hl()
			player.print_players_data(self.players,11,len(self.players))

	def team_deacay(self):
		for player in self.players:
			player.offense -= randint(0,3)
			player.defense -= randint(0,3)
			player.power -= randint(0,3)
			player.endurance -= randint(0,3)
		self.set_current_strength()

	def state_change(self):
		
		for player in self.players[0:11]:
			player.state_decay()
		
		for player in self.players[11:]:
			player.state_recovery()

	def injury(self):
		
		injured_players = []
		
		for player in self.players[0:11]:
			if player.injury_chance() == True:
				player.injury_d = randint(2,5)
				injured_players.append(player)
		
		return injured_players

	def count_injured_players(self):
		
		injured_players = 0
		
		for player in self.players:
			if player.injury_d > 0:
				injured_players += 1

		return injured_players

	def ageing_players(self):
		for i in range(0, len(self.players)):
			self.players[i].age = self.players[i].age + 1

	def train(self):
		train_team = training.Training(self)
		train_team.train_feature(self.trained_feature)

	def swap_player(self):
		if len(self.players) < 12:
			print "You do not have enought players for substitution!"

		elif len(self.players) >= 12:
			id_out = raw_input("Player to leave the active team: enter player ID (1-11): ")
			print ""
			id_in = raw_input("Player be included in the active team: enter player ID (12 - "+ str(len(self.players)) +"): ")
			print ""
			try:
				id_out = int(id_out) - 1
				if id_out in range (0,11):
					try:
						id_in = int(id_in) - 1
						if id_in in range (11, len(self.players)):
							self.players[id_out], self.players[id_in] = self.players[id_in], self.players[id_out]
							self.set_current_strength()
							print "Your players have been swapped!"
						else:
							print "Invalid player ID! Valid IDs: 12-"+ str(len(self.players)) +"."
					except ValueError:
						print "Input error!"
						print ""
						return
				else:
					print "Invalid player ID! Valid IDs: 1-11."
			except ValueError:
				print "Input error!"
				print ""
				return

	def condition_md_team(self):

		goalies = 0

		active_players = self.players[0:11]

		#Checking amount of active players:
		if active_players < 11:
			print "You need minimum of 11 active players"
			return False

		#Checking for injured players:
		for player in active_players:
			if player.injury_d > 0:
				print "You have to substitue your injured player(s)"
				return False

		#Checking for amount of goalkeepers:
		for player in active_players:
			if player.position == 0:
				goalies += 1
		if goalies < 1:
			print "You need at least one Goalkeeper"
			return False
			
		elif goalies > 1:
			print "You can only draft one Goalkeeper"
			return False

		return True

def sort_teams(teams):
	teams_sorted_diff = sorted(teams, key=lambda team:team.get_diff_goals(), reverse=True)
	teams_sorted_points = sorted(teams_sorted_diff, key=attrgetter('points'), reverse=True)
	
	return teams_sorted_points

def sort_teams_by_title(teams):

	teams_sorted_title = sorted(teams, key=attrgetter('title'), reverse=True)
	
	return teams_sorted_title

def get_teams_from_text(file_name, index):
	
	"""
	Method to retrieve a list of team instances from a text file
	Input: index, representing the amount of teams to get from the text file
	Output: list of instances of object Team
	"""

	teams = []
	List = open("teams/" + file_name + ".txt",'r').read().splitlines()
	
	j = 0
	for i in range(0,len(List)):
		if j < index:
			dummy_team = Team(List[i], "Wappen")
			teams.append(dummy_team)
		j = j+1
	return teams

def get_teams_from_league(teams, league):
	
	"""Returns a list of Teams from the requested league"""
	
	teams_1 = []
	for i in range(0,len(teams)):
		if teams[i].league == 1:
			teams_1.append(teams[i])

	return teams_1

def get_team_names_in_list(teams):
	team_names = []
	for i in range (0,len(teams)):
		team_names.append(teams[i].name)
	return team_names

def get_team_from_list(teams, team_name):
	for i in range(0,len(teams)):
		if teams[i].name == team_name:
			return teams[i]

def eq_name(team_a,team_list):
	
	"""This method compares the name of an instance Team to names of a list of instances Team
	"""
	
	for i in range (0,len(team_list)):
		if team_a.name == team_list[i].name:
			return True
	else:
		return False

def set_league(teams, l):
	"""With this function, it is possible to set the league of a list of instances of Team
	input: list of Team instances and an integer in range [1,10]
	output: list of Team instances"""
	
	#~ print teams[0].name
	
	if l>0 and l<10:
		for team in teams:
			team.league = l
		
	else:
		print("Error! Only leagues between 1 and 9 can be set.")
	
	return teams

def print_top_scorers(teams):
	
	"""Prints the table of top scoring players
	input: list ofinstances of object Team
	output: printed list of top scoring players"""
	
	all_players = []
	
	for i in range(0,len(teams)):
		for j in range(0, len(teams[i].players)):
			all_players.append(teams[i].players[j])
		
	players_sorted_score = sorted(all_players, key=attrgetter('shot_goals'), reverse=True)
	
	for player in players_sorted_score:
		if player.shot_goals > 0:
			print(player.first_name + " " + player.last_name + " - " + player.team + " : " + str(player.shot_goals))

def print_teams_by_titles(teams):
	teams_sorted = sort_teams_by_title(teams)
	
	print "{:2}#  | {:19.19}Team | {:1}T".format("","","")
	
	j = 0
	
	for i in range(0,len(teams_sorted)):
		if teams_sorted[i].title > 0:
			j = j+1
			print "{pos:3}. | {tname:23.23} | {tt:2}".format(pos = j,
															tname = teams_sorted[i].name, 
															tt = teams_sorted[i].title)
	print ""

def print_teams(teams):
	for i in range (0,len(teams)):
		print "{no:3}. | {tname:23.23}".format(no = i+1,
											tname = teams[i].name)

def run_sell_player(season_1):
	
	s = season_1.get_season_count()
	
	print ""
	print "Your current team: "
	season_1.manager.team.print_players()
	print ""
	print "Your currently available funds are: " + str(season_1.manager.team.finances.cash)
	print ""
	if len(season_1.manager.team.players) < 12:
		print "You cannot sell any players, as you need a minimum of 11 players."
		return
	
	elif len(season_1.manager.team.players) >= 12:
		print "Which player would you like to sell? Please input the related ID"
		user_input = raw_input("Press Enter to return to Main Menu...")

	try:
		user_input = int(user_input)
		user_input -= 1

		if user_input in range (0,len(season_1.manager.team.players)):
			print ""
			print "You sold your player " + season_1.manager.team.players[user_input].first_name + " " + season_1.manager.team.players[user_input].last_name +" at a prize of " + str(season_1.manager.team.players[user_input].market_value) + "."
			season_1.manager.team.finances.try_transaction(0,season_1.manager.team.players[user_input].market_value,s)
			sold_player = season_1.manager.team.players[user_input]
			sold_player.team = ""
			season_1.players_fh.append(sold_player)
			season_1.manager.team.players.pop(user_input)

		else:
			print "Invalid input ID"
			run_sell_player(season_1)

	except ValueError:
		menues.run_mainmenu(season_1)

def run_buy_player(season_1):

	s = season_1.get_season_count()

	print ""
	print "Your current team: "
	season_1.manager.team.print_players()
	print ""
	print "Your currently available funds are: " + str(season_1.manager.team.finances.cash)
	print ""
	print "Players available for hiring: "
	player.print_players(season_1.players_fh)
	print ""
	print "In case you would like to hire one of the players, please input the related ID"
	user_input = raw_input("Press Enter to return to Main Menu...")

	try:
		user_input = int(user_input)
		user_input -= 1

		if user_input in range (0,len(season_1.players_fh)):
			opp = season_1.manager.team.finances.try_transaction(season_1.players_fh[user_input].market_value, 0, s)
			if opp == True:
				print "You have bought player " + season_1.players_fh[user_input].first_name + " " + season_1.players_fh[user_input].last_name + " for EURO " + str(season_1.players_fh[user_input].market_value) + "."
				season_1.players_fh[user_input].team = season_1.manager.team.name
				season_1.manager.team.players.append(season_1.players_fh[user_input])
				season_1.players_fh.pop(user_input)
			elif opp == False:
				return

		else:
			print "Invalid input ID"
			run_buy_player(season_1)

	except ValueError:
		menues.run_mainmenu(season_1)

def run_sell_trainer(season_1):

	s = season_1.get_season_count()

	print ""
	print "Your current trainer is: "
	trainer.print_trainers(season_1.manager.team.trainers)
	print ""
	print "Your currently available funds are: " + str(season_1.manager.team.finances.cash)
	print ""
	
	if len(season_1.manager.team.trainers) < 2:
		print "You cannot sell any trainer, as you need a minimum of 1 trainer."
		return

	elif len(season_1.manager.team.trainers) >= 2:
		print "Which trainer would you like to sell? Please input the related ID"
		user_input = raw_input("Press Enter to return to Main Menu...")

	try:
		user_input = int(user_input)
		user_input -= 1

		if user_input in range (0,len(season_1.manager.team.trainers)):
			print ""
			print "You sold your trainer " + season_1.manager.team.trainers[user_input].first_name + " " + season_1.manager.team.trainers[user_input].last_name +" at a prize of " + str(season_1.manager.team.trainers[user_input].market_value) + "."
			season_1.manager.team.finances.try_transaction(0,season_1.manager.team.trainers[user_input].market_value,s)
			sold_trainer = season_1.manager.team.trainers[user_input]
			season_1.trainers_fh.append(sold_trainer)
			season_1.manager.team.trainers.pop(user_input)


		else:
			print "Invalid input ID"
			run_sell_player(season_1)

	except ValueError:
		menues.run_mainmenu(season_1)
	

def run_buy_trainer(season_1):

	s = season_1.get_season_count()

	#~ trainers_for_hiring = trainer.get_random_trainers(randint(1,10))
	
	print ""
	print "Your current trainer is: "
	trainer.print_trainers(season_1.manager.team.trainers)
	print ""
	print "Your currently available funds are: " + str(season_1.manager.team.finances.cash)
	print ""
	print "Trainers available for hiring: "
	trainer.print_trainers(season_1.trainers_fh)
	#~ trainer.print_trainers(trainers_for_hiring)
	print ""
	print "In case you would like to hire one of the trainers, please input the related ID"
	user_input = raw_input("Press Enter to return to Main Menu...")

	try:
		user_input = int(user_input)
		user_input -= 1

		if user_input in range (0,len(season_1.trainers_fh)):
			opp = season_1.manager.team.finances.try_transaction(season_1.trainers_fh[user_input].market_value, 0, s)
			if opp == True:
				print "You have bought trainer " + season_1.trainers_fh[user_input].first_name + " " + season_1.trainers_fh[user_input].last_name + " for EURO " + str(season_1.trainers_fh[user_input].market_value) + "."
				season_1.manager.team.trainers.append(season_1.trainers_fh[user_input])
				season_1.trainers_fh.pop(user_input)
			elif opp == False:
				return

		else:
			print "Invalid input ID"
			run_buy_trainer(season_1)

	except ValueError:
		menues.run_mainmenu(season_1)

