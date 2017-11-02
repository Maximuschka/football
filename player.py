#~ from __future__ import division
import random

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
		self.shot_goals = 0
		self.help_p = 0

	def get_strength(self):
		strength = self.offense + self.defense + self.power + self.endurance
		strength = strength / 4
		return strength

	def set_first_name(self):
		List = open("player/first_names.txt",'r').read().splitlines()
		return random.choice(List)

	def set_last_name(self):
		List = open("player/last_names.txt",'r').read().splitlines()
		return random.choice(List)
