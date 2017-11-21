#~ from __future__ import division
from operator import itemgetter, attrgetter, methodcaller
from random import randint
import game

class Finances:

	def __init__(self,team):
		self.team = team
		self.cash = 100000
		self.credit = 0
	
	#~ def get_init_cash(self):
		#~ init_cash = 100000 / self.team.league
		#~ print self.team.league
		#~ print init_cash
		#~ return init_cash

	def set_matchday_cash_won(self):
		
		new_cash = 1000 / self.team.league
		self.cash = self.cash + new_cash
		
	def set_matchday_cash_draw(self):

		new_cash = (1000 / self.team.league)/2
		self.cash = self.cash + new_cash

	def set_matchday_cash_stadium(self):
		
		"""
		This method calculates the income from a home match.
		!!!It consideres the stadium to always be SOLD OUT!!!
		"""
		
		stadium_income = self.team.stadium.capacity * self.team.stadium.ticket_prize
		self.team.finances.cash = self.team.finances.cash + stadium_income
	
	def print_finances(self):
		print "Team finances of team " + self.team.name
		print ""
		print "Current available cash: " + str(self.cash)

def set_matchday_cash(game):

	"""
	In diese Funktion sollten auch die Stadioneinnahmen fuer die Heimmannschaft
	"""
	
	game.team_a.finances.set_matchday_cash_stadium()
	
	if game.score_team_a > game.score_team_b:
		game.team_a.finances.set_matchday_cash_won()

	elif game.score_team_a == game.score_team_b:
		game.team_a.finances.set_matchday_cash_draw()
		game.team_b.finances.set_matchday_cash_draw()
		
	elif game.score_team_a < game.score_team_b:
		game.team_b.finances.set_matchday_cash_won()

#~ def get_credit(amount, interest):
