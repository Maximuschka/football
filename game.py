#leo was here!

import team
import random
from operator import itemgetter, attrgetter, methodcaller 

class Game:

	def __init__(self,team_a,team_b):
		self.team_a = team_a
		self.team_b = team_b
		self.score_team_a = 0
		self.attempts_team_a = 0
		self.score_team_b = 0
		self.attempts_team_b = 0

	#~ def print_result(self):
		
		#~ print("")

def game_improved(team_a, team_b):

	"""Method to calculate the results of a game between two teams. Method sets different instance parameters, based on game results
	Input: two Team instances
	Outpt: two Team instances"""

	if team_a.training_status == True:
		team_a.train(0)
		team_a.train(1)
		team_a.train(2)
		team_a.train(3)

	if team_b.training_status == True:
		team_b.train(0)
		team_b.train(1)
		team_b.train(2)
		team_b.train(3)

	game1 = Game(team_a,team_b)
	team_a.set_tactic_random()
	team_b.set_tactic_random()
	
	i = 0
	chances = random.randint(10,25)
	
	while(i<chances):
		chance_for_team_a = chance(team_a, team_b)
		score_chance_a = score(5, team_a)
		score_chance_b = score(5, team_b)
		
		if(chance_for_team_a == True):
			game1.attempts_team_a = game1.attempts_team_a + 1
		
		if(chance_for_team_a == True and score_chance_a == True):
			game1.score_team_a = game1.score_team_a + 1
			team_a = scoring_player(team_a)
			
		if(chance_for_team_a == False):
			game1.attempts_team_b = game1.attempts_team_b + 1
		
		if(chance_for_team_a == False and score_chance_b == True):
			game1.score_team_b = game1.score_team_b + 1
			team_b = scoring_player(team_b)

		i = i +1
		
	team_a.scored_goals = team_a.scored_goals+game1.score_team_a
	team_a.received_goals = team_a.received_goals+game1.score_team_b
	
	team_b.scored_goals = team_b.scored_goals+game1.score_team_b
	team_b.received_goals = team_b.received_goals+game1.score_team_a

	team_a.attempts = team_a.attempts+game1.attempts_team_a
	team_b.attempts = team_b.attempts+game1.attempts_team_b

	team_a.games_played = team_a.games_played+1
	team_b.games_played = team_b.games_played+1

	if game1.score_team_a > game1.score_team_b:
		team_a.points = team_a.points+3
		if team_a.moral < 4:
			team_a.moral = team_a.moral+1
		if team_b.moral > 0:
			team_b.moral = team_b.moral-1
	elif game1.score_team_a == game1.score_team_b:
		team_a.points = team_a.points+1
		team_b.points = team_b.points+1
	elif game1.score_team_a < game1.score_team_b:
		team_b.points = team_b.points+3
		if team_b.moral < 4:
			team_b.moral = team_b.moral+1
		if team_a.moral > 0:
			team_a.moral = team_a.moral-1
	
	#Output - Teamnames and Scores
	print "{ta:23} |{g1} : {g2}| {tb:>23}".format(ta = team_a.name, tb = team_b.name, g1 = game1.score_team_a , g2=game1.score_team_b)

	return(game1)

def chance(team_a, team_b):

	"""For a given scoring attempt, this method calculates based on different team specific paramters, which team get the chance to score
	Input: two instances of object Team
	Output: bool"""

	while True:		

		chance_a = random.randrange(1,80) + team_a.strength/4 + team_a.tactic + team_a.moral
		chance_b = random.randrange(1,80) + team_b.strength/4 + team_b.tactic + team_b.moral

		if chance_a > chance_b:
			return True
		
		if chance_a < chance_b:
			return False

def score(percent, team):
	
	"""Gibt aus, ob eine Chance zu einem Treffer verwandelt wird
	Je hoeher x, desto geringer ist die Chance einen Treffer zu erzielen
	Input: Ein prozentualer Wert, mit dem die Wahrscheinichkeit beeinflusst werden kann und eine Instanz von Team
	Output: bool"""
	
	x = 600
	percent_adapt = percent + team.strength + team.tactic + team.moral
	return random.randrange(x) < percent_adapt

def scoring_player(team):

	"""Method, defining the specific player that has scored a goal, based on different parameters describing the player (position, strength and a random parameter)
	Input: instance of object Team
	Output: instance of object Team"""

	for i in range(0,len(team.players)):
		team.players[i].help_p = team.players[i].position * (random.randint(0,10) + team.players[i].strength/5)
		
	scorer = []
	scorer = sorted(team.players, key=attrgetter('help_p'), reverse=True)
	
	for i in range(0,len(team.players)):
		if (scorer[0].first_name == team.players[i].first_name and scorer[0].last_name == team.players[i].last_name and scorer[0].age == team.players[i].age):
			team.players[i].shot_goals = team.players[i].shot_goals + 1

	return team
