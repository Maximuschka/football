#~ from __future__ import division
from operator import itemgetter, attrgetter, methodcaller
from random import randint
import game

class Stadium:

	def __init__(self, team):
		self.team = team
		self.capacity = 1000
		self.ticket_prize = 5
	
	def set_ticket_prize(self, ticket_prize):
		self.ticket_prize = ticket_prize

	def add_capacity(self, added_capacity):
		cost_per_seat = 100
		cost_tot = added_capacity * cost_per_seat
		
		if cost_tot <= self.team.finances.cash:
			self.capacity = self.capacity + added_capacity
			self.team.finances.cash = self.team.finances.cash - cost_tot

		elif cost_tot > self.team.finances.cash:
			print "Insufficient cash!"
	
	def print_stadium_info(self):
		print ""
		print "The stadium of " + self.team.name + " has a capacity of " + str(self.capacity) + "."
		print ""
		print "Current ticket prize is: " + str(self.ticket_prize) + "."

	def request_new_ticket_prize(self):
		print ""
		new_ticket_prize = input("Please enter the new ticket prize (value between 0 and 20)")
		
		if new_ticket_prize in range (0,20):
			self.set_ticket_prize(new_ticket_prize)
		
		else:
			print "Ticket prize is too high."
			return
	
	def get_income(self):
		income = self.capacity * self.ticket_prize
		return income
