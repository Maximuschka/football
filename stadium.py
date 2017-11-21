#~ from __future__ import division
from operator import itemgetter, attrgetter, methodcaller
from random import randint
import game

class Stadium:

	def __init__(self, team):
		self.team = team
		self.capacity = 1000
		self.ticket_prize = 5
	
	def add_capacity(self, added_capacity):
		cost_per_seat = 100
		cost_tot = added_capacity * cost_per_seat
		
		if cost_tot <= self.team.finances.cash:
			self.capacity = self.capacity + added_capacity
			self.team.finances.cash = self.team.finances.cash - cost_tot

		elif cost_tot > self.team.finances.cash:
			print "Insufficient cash!"
