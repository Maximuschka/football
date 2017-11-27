import game
import matchday
import table
#~ import test
import league
import team
import menues

class Season:

	"""
	Central Class to process and store all information related to the football manager
	"""

	def __init__(self):
		self.year = 2015
		self.matchday = 0
		self.matchdays = []
		self.teams = []
		self.leagues = []
		self.manager = ""
		self.et = table.Table("Eternal Table")
		
	def add_matchday(self, matchday):
		
		"""Adding a single match day to the season"""
		
		self.matchdays.append(matchday)
	
	def set_new_season_matches(self):
		for i in range (0,len(self.leagues)):
			self.leagues[i].first_leg = get_first_leg(self.leagues[i].teams)
			self.leagues[i].second_leg = get_second_leg(self.leagues[i].teams)

	def set_next_year(self):
		self.year = self.year + 1
		
	def add_teams(self, teams):
		self.teams = teams
		self.leagues = league.teams_to_leagues(self.teams)
	
	def add_manager(self, manager):
		self.manager = manager

def run_season_md(season):
	
	"""
	Calculates all results of one matchday and prints the tables of all leagues played in that matchday
	Input: instance of object season
	Output: printed results and table of all leagues
	"""
		
	md = season.matchday

	if md == 0:
		season = new_season(season)

	s = season.year - 2016
	menues.run_mainmenu(season)

# i = Spieltag
# j = Spiel / Spieltag

	"""Kleines Problem: Aktuell muessen alle Ligen gleich viele Teams haben (siehe folgende while Schliefe mit Iterator i)"""

	if md < (len(season.leagues[0].teams))-1:
		for k in range (0,len(season.leagues)):
			
			j = 0

			print(str(md+1) + ". Spieltag - " + str(k+1) + ". Liga")
			print("")

			while(j < len(season.leagues[k].teams)/2):
				
				game.game_improved(season.leagues[k].first_leg[md][j][0], season.leagues[k].first_leg[md][j][1], season.year, season.matchday)
				
				j = j+1

			print""
			table.print_table(season.leagues[k].teams)
			print "_____________________________________________"
			print ""
		
		print ""

	if md >= (len(season.leagues[0].teams))-1:
		md_sl = md - (len(season.leagues[0].teams))-1

		for k in range (0,len(season.leagues)):
			
			j = 0

			print(str(md+1) + ". Spieltag - " + str(k+1) + ". Liga")
			print("")

			while(j < len(season.leagues[k].teams)/2):
				
				game.game_improved(season.leagues[k].second_leg[md_sl][j][0], season.leagues[k].second_leg[md_sl][j][1], season.year, season.matchday)
				
				j = j+1

			print("")
			table.print_table(season.leagues[k].teams)
			print "_____________________________________________"
			print ""
		
		print ""

	season.matchday = season.matchday + 1

	if season.matchday < (len(season.leagues[0].teams)-1)*2:
		for i in range (0,len(season.leagues)):
			for j in range (0,len(season.leagues[i].teams)):
				season.leagues[i].teams[j].finances.cost_mds[s].append(0)
				season.leagues[i].teams[j].finances.income_mds[s].append(0)

	if season.matchday == (len(season.leagues[0].teams)-1)*2:

		season.matchday = 0

		for k in range (0,len(season.leagues)):
			if season.leagues[k].teams[0].league == 1:
				teams_sorted = team.sort_teams(season.leagues[k].teams)
				teams_sorted[0].title = teams_sorted[0].title + 1
		
		print "Meister " + str(season.year) + ": " + teams_sorted[0].name
		print ""
		
		season.et = table.update_eternal_table(season.et, season.leagues[0].teams)
		league_rise_descent(2,2,season)

def new_season(season):

	"""
	Sets back parameters to initial values (reset for beginning of season)
	Input: instance of object season
	Output: instance of object season
	"""
	
	season.set_next_year()
	season.set_new_season_matches()

	s = season.year - 2016
	
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
			team.finances.cost_mds.append([])
			team.finances.cost_mds[s].append(0)
			team.finances.income_mds.append([])
			team.finances.income_mds[s].append(0)

	return season

def league_rise_descent(r,d, season):
	
	"""
	Method setting the season.league parameter depending on rise and descent of the past season
	input: instance of object season, integer for number of teams rising (r) and number of teams descending (d)
	output: manipulation of season.league paramter
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

	"""
	calculates fixtures for an entire season
	Input: list of instances of object Team
	Output: list of tuples of fixtures
	"""

	if len(teams) % 2:
		teams.append('Day off')  # if team number is odd - use 'day off' as fake team     

	rotation = list(teams)       # copy the list
    
	fixtures = []
	for i in range(0, len(teams)-1):
		fixtures.append(rotation)
		rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

	return fixtures
	

def get_first_leg(teams):
	
	"""
	Sets the matches for first leg of a season
	Input: List of tuples of instances of object team
	Output: List of lists of tuples of instances of object team (array of set matches)
	"""
	
	matches = fixtures(teams)
	set_matches = []

	for f in matches:
		n = len(f)
		set_matches.append(zip(f[0:n/2],reversed(f[n/2:n])))

	return set_matches

def get_second_leg(teams):

	"""
	Sets the matches for second leg of a season
	Input: List of tuples of instances of object team
	Output: List of lists of tuples of instances of object team (array of set matches)
	"""

	matches = fixtures(teams)
	set_matches = []

	for f in matches:
		n = len(f)
		set_matches.append(zip(f[0:n/2],reversed(f[n/2:n])))

	set_reverse_matches = swap_teams_matches(set_matches, len(teams))

	return set_reverse_matches

def swap_teams_matches(swapped_matches, length):
	
	"""
	reverses the two oponents in a single game, for all games
	input is a list of a list of tuples (a) and an integer giving the amount of teams
	output is a list of a list of tuples
	"""

	for i in range(0, length-1):
		for j in range(0, length/2):
			swapped_matches[i][j] = swapped_matches[i][j][1], swapped_matches[i][j][0]
			#~ swapped_matches[i][j] = tuple(reversed(swapped_matches[i][j]))

	return swapped_matches

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
