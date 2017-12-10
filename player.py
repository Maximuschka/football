from __future__ import division
import random
import season
import menues

class Player:

	def __init__(self, team_category):
		self.first_name = self.set_first_name()
		self.last_name = self.set_last_name()
		self.age = random.randint(16,35)
		self.team = ""
		self.position = ""
		self.state = 100
		self.offense = team_category + random.randint(0,30)
		self.defense = team_category + random.randint(0,30)
		self.agression = random.randint(0,100)
		self.power = team_category + random.randint(0,30)
		self.endurance = team_category + random.randint(0,30)
		self.strength = self.get_strength()
		self.market_value = self.get_market_value()
		self.salary = 0
		self.shot_goals = 0
		self.shot_goals_career = 0
		self.help_p = 0
		self.injury_d = 0

	def get_strength(self):
		strength = self.state/100 * (self.offense + self.defense + self.power + self.endurance)
		strength = strength / 4
		return strength

	def get_market_value(self):
		market_value = self.strength * 1000
		return market_value

	def set_salary(self, team_league):
		self.salary = ((self.offense + self.defense + self.power + self.endurance) * 3) / team_league

	def set_first_name(self):
		List = open("player/first_names.txt",'r').read().splitlines()
		return random.choice(List)

	def set_last_name(self):
		List = open("player/last_names.txt",'r').read().splitlines()
		return random.choice(List)

	def set_random_position(self):
		self.position = random.randint(0,3)

	def set_current_strength(self):
		self.strength = self.get_strength() 

	def print_injury(self):
		
		return " " + str(self.injury_d) + " "
		
		if self.injury_d == 0:
			return "   "
		elif self.injury_d > 0:
			return " + "

	def injury_chance(self):
		age_chance = self.age / 40

		m = -0.009
		n = 1
		state_chance = m * self.state + n

		#In worst case scenario (age = 40, state = 0), there is a 10 % chance for an injury:
		base_chance = (age_chance + state_chance) * 5
		return base_chance > random.randint(0,100)

	def new_matchday_injury_d(self):
		self.injury_d -= 1

	def state_decay(self):
		age_chance = self.age / 40
		end_chance = 1 - (self.endurance / 100)

		base_chance = age_chance + end_chance

		if 0 < base_chance < 0.8:
			self.state -= random.randint(1,3)
		elif 0.8 <= base_chance < 1.2:
			self.state -= random.randint(1,5)
		elif 1.2 <= base_chance < 2:
			self.state -= random.randint(2,7)

	def state_recovery(self):
		self.state += (random.randint(2,5))
		if self.state > 100:
			self.state = 100

def get_random_players(n):

	players = []

	for i in range (0,n):
		dummy_player = Player(random.randint(15,75))
		dummy_player.set_random_position()
		players.append(dummy_player)

	return players

def delete_random_players(players,n):
	
	"""
	n - amount of player to be deleted
	"""
	
	for i in range (0,n):
		del_id = random.randint(0,len(players)-1)
		players.pop(del_id)

def print_players(players):
	print_players_hl()
	print_players_data(players,0,len(players))

def print_players_hl():
	print "{:2}#  | {:<8}FN {:<13.13}LN | {:3}S | {:2}G | {:1}CG | {:2}A | {:2}P | {:1}ST | {:6}PR | {:1}IN ".format("", "","","","","","","","","","")

def print_players_data(players,s,e):

	"""
	s - start
	e - end
	"""

	for i in range(s, e):
		print "{no:3}. | {pfn:10} {pln:15.15} | {stn:3.1f} | {gos:3} | {goc:3} | {age:3} | {pos:3} | {sta:3} | {pri:8} | {inj:3} ".format(no = i+1,
																								pfn = players[i].first_name,
																								pln = players[i].last_name,
																								stn = players[i].strength,
																								gos = players[i].shot_goals,
																								goc = players[i].shot_goals_career,
																								age = players[i].age,
																								pos = players[i].position,
																								sta = players[i].state,
																								inj = players[i].print_injury(),
																								pri = players[i].market_value)


def delete_old_players(players):
	i = 0
	while i < len(players):
		if players[i].age >= 40:
			players.pop(i)
			i -= 1
		i += 1

def get_youth_players(team):

	youth_players = []
	
	for i in range (0,random.randint(1,3)):
		dummy_player = Player(random.randint(30,70))
		dummy_player.team = team.name
		dummy_player.age = random.randint(16,20)
		dummy_player.set_random_position()
		youth_players.append(dummy_player)

	return youth_players
