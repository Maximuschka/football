#~ from __future__ import division
from operator import itemgetter, attrgetter, methodcaller
from random import randint
import player
import training
import trainer
import finances
import stadium
import operator

class Team:

	def __init__(self, name, wappen_image):
		self.category = randint(35,70)
		self.name = name
		self.wappen = wappen_image
		self.trainer = self.add_trainer()
		self.training_status = False
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
		self.home_md = False
		#~ self.cost_matchdays = []
		#~ self.income_matchdays = []

		#Team category - good (70) or bad (35) - influences player strength when initiating Players

	def get_name(self):
		return self.name

	def get_efficiency(self):
		if (self.attempts > 0):
			eff = (self.scored_goals / self.attempts)*100
			return eff
		
		else:
			return 0

	def get_strength(self):
		
		strength = 0

		for i in range (0, len(self.players)):
			strength = strength + self.players[i].strength

		return strength/len(self.players)

	def get_diff_goals(self):
		diff_goals = self.scored_goals - self.received_goals
		return diff_goals

	def get_income_match_won(self):
		income = 1000 / self.league
		return income

	def get_income_match_draw(self):
		income = (1000 / self.league)/2
		return income

	#~ def set_cost_matchday(self):

		#~ """WORK IN PROGRESS"""

		#~ dummy_cost = 0
		#~ for player in self.players:
			#~ dummy_cost = dummy_cost + player.get_salary()

		#~ dummy_cost = dummy_cost + self.trainer.get_salary()

		#~ self.cost_matchdays.append(dummy_cost)

	#~ def set_income_matchday(self):

		#~ """WORK IN PROGRESS"""

		#~ dummy_income = 0
		
		#~ if self.home_md == True:
			#~ stadium_income = self.stadium.capacity * self.stadium.ticket_prize
			#~ dummy_income += stadium_income
		
		#~ self.income_matchdays.append(dummy_income)

	def set_training_status(self, status):
		self.training_status = status

	def set_trained_feature(self, feature):
		self.trained_feature = feature

	def set_current_strength(self):
		self.strength = self.get_strength() 

	def set_tactic_random(self):
		self.tactic = randint(0,2)
		
	def set_positions(self):
		self.players[0].position = 0
		for i in range(1, 5):
			self.players[i].position = 1
		for i in range(5, 9):
			self.players[i].position = 2
		for i in range(9, 11):
			self.players[i].position = 3

	def add_players(self):
		players = []
		for i in range(0,11):
			player1 = player.Player(self.category)
			player1.team = self.name
			players.append(player1)
		return players
	
	def add_trainer(self):
		trainer1 = trainer.Trainer()
		return trainer1
	
	#~ def add_finances(self):
		
	
	def print_players(self):
		print "{:2}#  | {:<8}FN {:<13.13}LN | {:2}S | {:2}G | {:2}A | {:2}P".format("","","","","","","")
		for i in range(0, len(self.players)):
			print "{no:3}. | {pfn:10} {pln:15.15} | {stn:3} | {goa:3} | {age:3} | {pos:3}".format(no = i+1,
																									pfn = self.players[i].first_name,
																									pln = self.players[i].last_name,
																									stn = self.players[i].strength,
																									goa = self.players[i].shot_goals,
																									age = self.players[i].age,
																									pos = self.players[i].position)

			#~ print(str(i+1) + ". " + self.players[i].first_name + " " + self.players[i].last_name + " - Staerke: " + str(self.players[i].strength) + " - Offensive: " + str(self.players[i].offense) + " - Tore: " + str(self.players[i].shot_goals) + " - Alter: " + str(self.players[i].age) + " - Position: " + str(self.players[i].position))

	def ageing_players(self):
		for i in range(0, len(self.players)):
			self.players[i].age = self.players[i].age + 1

	def train(self):
		train_team = training.Training(self)
		train_team.train_feature(self.trained_feature)

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
	#~ List = open("teams/teams.txt",'r').read().splitlines()
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
