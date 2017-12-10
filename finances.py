#~ from __future__ import division
from operator import itemgetter, attrgetter, methodcaller
from random import randint
import game
import team

class Finances:

	def __init__(self,team):
		self.team = team
		self.cash = 100000
		self.credit = 0
		self.cost_mds = []
		self.income_mds = []
 
	def print_finances(self, season_1):

		s = season_1.get_season_count()

		tot_income = self.get_tot_income(s)
		tot_cost = self.get_tot_cost(s)

		print "Team finances of team " + self.team.name
		print ""
		print "Current available cash: " + str(self.cash)
		print ""
		print "Income and Cost year: " + str(season_1.year)
		print "{:2}MD|{:4}Income|{:6}Cost".format("","","")
		
		for i in range (0,len(self.cost_mds[s])):

			print "{md:4}|{ic:10}|{co:10}".format(md = i+1,
													ic = int(self.income_mds[s][i]),
													co = int(self.cost_mds[s][i]))
		#~ print "{:5}TOT |{toti:10.10} | {totc:10.10}".format("",
														#~ toti = self.get_tot_income(s),
		print "{:1}TOT|{toti:10}|{totc:10}".format("",
											toti = int(tot_income),
											totc = int(tot_cost))
		print ""

	def get_tot_cost(self,s):
		
		tot_cost = 0
		
		for i in range (0, len(self.cost_mds[s])):
			tot_cost += self.cost_mds[s][i]
		
		return tot_cost

	def get_tot_income(self,s):
		
		tot_income = 0
		
		for i in range (0, len(self.income_mds[s])):
			tot_income = tot_income + self.income_mds[s][i]
		
		return tot_income

	def try_transaction(self, cost, income, s):

		if self.cash + income - cost >= 0:
			self.transaction(cost, income, s)
			return True
		
		else:
			print "Your funds are not sufficient for this transaction!"
			return False

	def transaction(self, cost, income, s):
		
		l = len(self.cost_mds[s]) - 1
		
		self.cash = self.cash + income
		self.income_mds[s][l] += income
		self.cash = self.cash - cost
		self.cost_mds[s][l] += cost

def set_finances_md(team, res_id, s, md):
	
	"""
	res_id:
	0 - won
	1 - draw
	2 - lost
	"""
	
	team.finances.cash += get_income_md(team, res_id, s, md)
	team.finances.cash -= get_cost_md(team, s, md)

def get_income_md(team, res_id, s, md):

	income_md = 0

	if team.home_md == True:
		income_md += team.stadium.get_income()

	if res_id == 0:
		income_md += team.get_income_match_won()
	elif res_id == 1:
		income_md += team.get_income_match_draw()

	team.finances.income_mds[s][md] += income_md

	return income_md

def get_cost_md(team, s, md):

	cost_md = 0

	for player in team.players:
		cost_md = cost_md + player.salary

	for trainer in team.trainers:
		cost_md = cost_md + trainer.salary

	team.finances.cost_mds[s][md] += cost_md

	return cost_md

def add_finance_lists(season):
	
	s = season.get_season_count()
	
	for i in range (0,len(season.leagues)):
		for team in season.leagues[i].teams:
			team.finances.cost_mds.append([])
			team.finances.cost_mds[s].append(0)
			team.finances.income_mds.append([])
			team.finances.income_mds[s].append(0)

#~ def get_credit(amount, interest):
