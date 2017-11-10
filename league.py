#~ from __future__ import division
import random
import season

class League:

	def __init__(self, teams):
		self.teams = teams
		self.level = self.get_level()
		self.all_matches = season.get_all_matches(self.teams)
	
	def get_level(self):
		dummy_level = self.teams[0].league
		for i in range (0,len(self.teams)):
			if dummy_level != self.teams[i].league:
				print "Error - the parsed teams have varying levels"
				return None
		
		return dummy_level

def teams_to_leagues(teams):
	teams_in_leagues = []
	teams_in_leagues = season.get_teams_in_leagues(teams)
	
	all_leagues = []
	
	for i in range (0,len(teams_in_leagues)):
		
		dummy_league = League(teams_in_leagues[i])
		all_leagues.append(dummy_league)
	
	return all_leagues
