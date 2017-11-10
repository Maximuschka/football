import game
import team
import matchday
import table
#import football
import test
import league

class Season:
	
	"""Class to store the information of a whole season"""

	def __init__(self, teams):
		self.year = 2015
		self.matchdays = []
		self.teams = teams
		self.leagues = league.teams_to_leagues(self.teams)
		
	def add_matchday(self, matchday):
		
		"""Adding a single match day to the season"""
		
		self.matchdays.append(matchday)
	
	def set_new_season_matches(self):
		for i in range (0,len(self.leagues)):
			self.leagues[i].all_matches = get_all_matches(self.leagues[i].teams)

	def set_next_year(self):
		self.year = self.year + 1

def season_different_leagues(season):
	
	"""calculates all results of a season and prints table after each game day
	Input: list of instances of object Team
	Output: printed results and table of each game day"""
	
	if season.leagues[0].teams[0].points > 0:
		league_rise_descent(2,2,season)
		
	run_season(season)

def run_season(season):
	
	"""calculates all results of a season and prints table after each game day
	Input: list of instances of object Team
	Output: printed results and table of each game day"""
	
	season = new_season(season)

	#~ s1_2017 = Season()

# i = Spieltag
# j = Spiel / Spieltag

	"""Kleines Problem: Aktuell muessen alle Ligen gleich viele Teams haben (siehe folgende while Schliefe mit Iterator i)"""

	for i in range (0,len(season.leagues[0].teams*2)-2):
		dummy_matchday = matchday.Matchday()
		
		for k in range (0,len(season.leagues)):
			
			j = 0

			print(str(i+1) + ". Spieltag - " + str(k+1) + ". Liga")
			print("")

			while(j < len(season.leagues[k].teams)/2):
				
				game.game_improved(season.leagues[k].all_matches[i][j][0], season.leagues[k].all_matches[i][j][1])
				#~ dummy_game = game.game_improved(season.leagues[k].all_matches[i][j][0], season.leagues[k].all_matches[i][j][1])
				#~ dummy_matchday.add_match(dummy_game)
				
				j = j+1

			#~ s1_2017.add_matchday(dummy_matchday)

			print("")
			table.print_table(season.leagues[k].teams)
			print("_____________________________________________")
			raw_input("Press Enter to continue...")
			print("")

	for i in range (0,len(season.leagues)):
		if season.leagues[i].teams[0].league == 1:
			teams_sorted = team.sort_teams(season.leagues[i].teams)
			teams_sorted[0].title = teams_sorted[0].title + 1
	
	print "Meister " + str(season.year) + ": " + teams_sorted[0].name

def new_season(season):
	"""sets back parameters to initial values
	Input: list of instances of object Team
	Output: list of parameters of object Team"""
	
	for i in range (0,len(season.leagues)):
	
		for team in season.leagues[i].teams:
			team.games_played = 0
			team.points = 0
			team.scored_goals = 0
			team.received_goals = 0
			team.attempts = 0
			for i in range(0, len(team.players)):
				team.players[i].shot_goals = 0
			team.set_positions()
			team.ageing_players()

	season.set_new_season_matches()
	
	season.set_next_year()

	return season

def league_rise_descent(r,d, season):
	
	"""
	input: list of instances of object Team, integer for number of teams rising (r) and number of teams descending (d)
	output: list of instances of object Team
	"""
	
	l = len(season.leagues)
	
	for i in range (0,l):
		teams_sorted = team.sort_teams(season.leagues[i].teams)

		if r > 0:
			i=0
			while i < r:
				if teams_sorted[i].league > 1:
					teams_sorted[i].league = teams_sorted[i].league - 1
				
					print "Aufsteiger aus " + str(teams_sorted[i].league+1) + ". Liga: " + teams_sorted[i].name
				i = i+1
		
		if d > 0:
			j=len(teams_sorted)-d
			while j < len(teams_sorted):
				if teams_sorted[j].league < l:
					teams_sorted[j].league = teams_sorted[j].league + 1
				
					print "Absteiger aus " + str(teams_sorted[j].league-1) + ". Liga: " + teams_sorted[j].name
				j = j+1
				print ""

	all_teams = get_list_of_teams_from_season(season)
	teams_in_leagues = get_teams_in_leagues(all_teams)
	
	for i in range (0,len(season.leagues)):
		season.leagues[i].teams = []
		season.leagues[i].teams.extend(teams_in_leagues[i])


def fixtures(teams):

	"""calculates fixtures for an entire season
	Input: list of instances of object Team
	Output: list of fixtures"""

	if len(teams) % 2:
		teams.append('Day off')  # if team number is odd - use 'day off' as fake team     

	rotation = list(teams)       # copy the list
    
	fixtures = []
	for i in range(0, len(teams)-1):
		fixtures.append(rotation)
		rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]
        
	return fixtures
	
def get_all_matches(teams):
	
	matches = fixtures(teams)
	set_matches = []

	for f in matches:
		n = len(f)
		set_matches.append(zip(f[0:n/2],reversed(f[n/2:n])))
	
	set_reverse_matches = swap_teams_matches(set_matches, len(teams))
	
	set_matches.extend(set_reverse_matches)
	
	return set_matches
	
def swap_teams_matches(set_matches, length):
	"""reverses the two oponents in a single game, for all games
	input is a list of a list of tuples (a) and an integer giving the amount of teams
	output is a list of a list of tuples"""

	for i in range(0, length-1):
		for j in range(0, length/2):
			set_matches[i][j] = set_matches[i][j][1], set_matches[i][j][0]
	
	return set_matches

def get_amount_leagues(teams):
	
	"""
	Method to return the amount of leagues different Team objects are realted to
	Input: list of Team instances
	Output: integer
	"""
	
	l = max(team.league for team in teams)

	return l

def get_teams_in_leagues(teams):
	
	"""
	Method to retrieve an array of lists of instances of object Team. Each iterate of the array is representing a list of Team objects,
	that are listed in the same league
	Input: list of Team instances
	Output: array of lists of Team instances
	"""
	
	l = get_amount_leagues(teams)
	
	teams_in_leagues = []
	
	for i in range (0,l):

		dummy_teams = []
		for team in teams:
			if team.league == i+1:
				dummy_teams.append(team)
		teams_in_leagues.append(dummy_teams)
	
	return teams_in_leagues

def get_list_of_teams_from_season(season):
	
	"""
	Method to retrieve all teams part of an object of class Season. These teams are taken from subclass League
	Input: instance of Season
	Output: list of instances of Team
	"""
	
	all_teams = []
	for i in range (0,len(season.leagues)):
		all_teams.extend(season.leagues[i].teams)

	return all_teams
