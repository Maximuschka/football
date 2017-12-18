#~ from __future__ import division
from operator import itemgetter, attrgetter, methodcaller
import random
import game
import menues

class Stadium:

	cost_per_seat = 100

	def __init__(self, team):
		self.team = team
		self.capacity = 1000
		self.capacity_constr = 0
		self.constr_done_md = 0
		self.construction = False
		self.ticket_prize = 5
	
	def set_ticket_prize(self, ticket_prize):
		self.ticket_prize = ticket_prize

	def start_construction(self, added_capacity, s, md, max_md):
		cost_tot = added_capacity * self.cost_per_seat
		
		if cost_tot <= self.team.finances.cash:
			self.capacity_constr = self.capacity + added_capacity
			self.capacity = self.capacity / 2

			dummy_md = md + (added_capacity / 100)
			if dummy_md > max_md:
				self.constr_done_md = dummy_md - max_md
			elif dummy_md <= max_md:
				self.constr_done_md = dummy_md

			self.team.finances.try_transaction(cost_tot, 0, s)
			self.construction = True


		elif cost_tot > self.team.finances.cash:
			print "Insufficient cash!"
	
	def end_construction(self,md):
		if self.constr_done_md == md:
			self.capacity = self.capacity_constr
			self.capacity_constr = 0
			self.constr_done_md = 0
			self.construction = False
		else:
			return

	def print_stadium_info(self):
		print ""
		print "The stadium of " + self.team.name + " has a capacity of " + str(self.capacity) + "."
		print ""
		print "Current ticket prize is: " + str(self.ticket_prize) + "."

	def request_new_ticket_prize(self):
		print ""
		new_ticket_prize = input("Please enter the new ticket prize (value between 0 and 20)")
		
		if new_ticket_prize in range (0,20
		):
			self.set_ticket_prize(new_ticket_prize)
		
		else:
			print "Ticket prize is too high."
			return
	
	def get_income(self, op_team):
		
		max_guests_md = self.get_guests_md(op_team)
		
		if self.capacity < max_guests_md:
			income = self.capacity * self.ticket_prize
		else: 
			income = max_guests_md * self.ticket_prize

		return income

	def get_guests_md(self, op_team):

		lim_prize = 20 / self.team.league
		
		if self.ticket_prize <= lim_prize:
			inf_ticket_prize = 0
		elif self.ticket_prize >  lim_prize:
			inf_ticket_prize = int((self.team.guest_potential*0.8) * (self.ticket_prize - lim_prize) / 15)
		inf_op_team = int((self.team.guest_potential / 4) * (30 / op_team.strength))
		inf_random = int((self.team.guest_potential / 8) * random.uniform(0, 1))
		max_guests_md = self.team.guest_potential - inf_ticket_prize - inf_op_team - inf_random

		if max_guests_md < 0:
			return 0
		else:
			return max_guests_md

def run_stadium_construction(season_1):
	print ""
	print "Construction prize per seat is " + str(season_1.manager.team.stadium.cost_per_seat)
	print ""
	print "Your currently available funds are: " + str(season_1.manager.team.finances.cash)
	print ""
	print "How many seats would you like to add? Enter number."
	user_input = raw_input("Press Enter to return to Main Menu...")

	try:
		user_input = int(user_input)
		if user_input > 0:
			season_1.manager.team.stadium.start_construction(user_input, season_1.get_season_count(), season_1.matchday, (len(season_1.leagues[0].teams)-1)*2)

		else:
			print "Invalid input ID"
			run_stadium_construction(season_1)

	except ValueError:
		menues.run_mainmenu(season_1)
