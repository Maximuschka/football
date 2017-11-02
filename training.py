#Max was here again

from operator import itemgetter, attrgetter, methodcaller
from random import randint
import player


class Training:

	def __init__(self, team):
		self.active = True
		self.team = team
	
	def train_feature(self,feature):
		if self.active == True:
			if feature == 0:
				self.train_offense()
			elif feature == 1:
				self.train_defense()
			elif feature == 2:
				self.train_power()
			elif feature == 3:
				self.train_endurance()
		#0 - train offense
		#1 - train defense
		#2 - train power
		#3 - train endurance

	def set_activity(self, activity):
		self.active = activity
	
	def train_offense(self):
		
		for player in self.team.players:
			if improv_chance(self.team.trainer.ability) == True:
				player.offense = player.offense + 1
				player.strength = player.get_strength()
		self.team.set_current_strength()

	def train_defense(self):
		for player in self.team.players:
			if improv_chance(self.team.trainer.ability) == True:
				player.defense = player.defense + 1
				player.strength = player.get_strength()
		self.team.set_current_strength()

	def train_power(self):
		for player in self.team.players:
			self.strength = self.team.get_strength()
			if improv_chance(self.team.trainer.ability) == True:
				player.power = player.power + 1
				player.strength = player.get_strength()
		self.team.set_current_strength()

	def train_endurance(self):
		for player in self.team.players:
			self.strength = self.team.get_strength()
			if improv_chance(self.team.trainer.ability) == True:
				player.endurance = player.endurance + 1
				player.strength = player.get_strength()
		self.team.set_current_strength()

def improv_chance(trainer):
	
	chance = randint(0,100)
	return chance < trainer
	
#propability is represented by a trainer. The better the trainer, 
#the higher the chance of improv
