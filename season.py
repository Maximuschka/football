import game
import team
import matchday
import table
import football
import test

class Season:
	
	"""Class to store the information of a whole season"""

	def __init__(self):
		self.year = ""
		self.matchdays = []
		self.leagues = ""
		
	def add_matchday(self, matchday):
		
		"""Adding a single match day to the season"""
		
		self.matchdays.append(matchday)

def run_season(teams):
	
	"""calculates all results of a season and prints table after each game day
	Input: list of instances of object Team
	Output: printed results and table of each game day"""

	teams = new_season(teams)
	
	matches = fixtures(teams)
	set_matches = []
	
	s1_2017 = Season()

	for f in matches:
		n = len(f)
		set_matches.append(zip(f[0:n/2],reversed(f[n/2:n])))
		
# i = Spieltag
# j = Spiel / Spieltag
# k = 
	i = 0

	while(i < len(teams)-1):
		j = 0
		dummy_matchday = matchday.Matchday()
		
		print(str(i+1) +". Spieltag")
		print("")
		while(j < len(teams)/2):
			
			dummy_game = game.game_improved(set_matches[i][j][0], set_matches[i][j][1])
			dummy_matchday.add_match(dummy_game)
			
			j = j+1

		s1_2017.add_matchday(dummy_matchday)

		i = i+1
		
		print("")
		table.print_table(teams)
		print("_____________________________________________")
		raw_input("Press Enter to continue...")
		print("")
	
	set_reverse_matches = swap_teams_matches(set_matches, len(teams))

	i = 0

	while(i < len(teams)-1):
		j = 0
		dummy_matchday = matchday.Matchday()

		print(str(i+1+len(teams)-1) +". Spieltag")
		print("")
		while(j < len(teams)/2):
			
			dummy_game = game.game_improved(set_reverse_matches[i][j][0], set_reverse_matches[i][j][1])
			dummy_matchday.add_match(dummy_game)

			j = j+1
		
		s1_2017.add_matchday(dummy_matchday)
		
		i = i+1

		print("")
		table.print_table(teams)
		print("_____________________________________________")
		raw_input("Press Enter to continue...")
		print("")

	if teams[0].league == 1:
		teams_sorted = team.sort_teams(teams)
		teams_sorted[0].title = teams_sorted[0].title + 1
		print ""
		print teams_sorted[0].name + " - Titel: " + str(teams_sorted[0].title)
		print ""

def season_different_leagues(teams):
	
	"""calculates all results of a season and prints table after each game day
	Input: list of instances of object Team
	Output: printed results and table of each game day"""
	
	if teams[0].points > 0:
		league_rise_descent(2,2,teams)
	
	
	all_teams = []
	all_teams = get_teams_in_leagues(teams)

	m = get_amount_leagues(teams)

	for i in range (0,m):
		print(str(i+1) + ".Liga")
		print("")
		run_season(all_teams[i])


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
	
def swap_teams_matches(set_matches, length):
	"""reverses the two oponents in a single game, for all games
	input is a list of a list of tuples (a) and an integer giving the amount of teams
	output is a list of a list of tuples"""

	for i in range(0, length-1):
		for j in range(0, length/2):
			set_matches[i][j] = set_matches[i][j][1], set_matches[i][j][0]
	
	return set_matches

def new_season(teams):
	"""sets back parameters to initial values
	Input: list of instances of object Team
	Output: list of parameters of object Team"""
	
	for team in teams:
		team.games_played = 0
		team.points = 0
		team.scored_goals = 0
		team.received_goals = 0
		team.attempts = 0
		for i in range(0, len(team.players)):
			team.players[i].shot_goals = 0
		team.set_positions()
		team.ageing_players()
	return teams

def league_rise_descent(r,d, teams):
	
	"""
	input: list of instances of object Team, integer for number of teams rising (r) and number of teams descending (d)
	output: list of instances of object Team"""
	
	teams_in_leagues = []
	teams_in_leagues = get_teams_in_leagues(teams)
	l = get_amount_leagues(teams)
	
	for i in range (0,l):
		teams_sorted = team.sort_teams(teams_in_leagues[i])

		if r > 0:
			i=0
			while i < r:
				if teams_sorted[i].league > 1:
					teams_sorted[i].league = teams_sorted[i].league - 1
				
				print(teams_sorted[i].name + " " + str(teams_sorted[i].league))
				i = i+1
		
		if d > 0:
			j=len(teams_sorted)-d
			while j < len(teams_sorted):
				if teams_sorted[j].league < l:
					teams_sorted[j].league = teams_sorted[j].league + 1
				
				print(teams_sorted[j].name + " " + str(teams_sorted[j].league))
				j = j+1

def get_amount_leagues(teams):
	l = max(team.league for team in teams)

	return l

def get_teams_in_leagues(teams):
	
	l = get_amount_leagues(teams)
	
	teams_in_leagues = []
	
	for i in range (0,l):

		dummy_teams = []
		for team in teams:
			if team.league == i+1:
				dummy_teams.append(team)
		teams_in_leagues.append(dummy_teams)
	
	return teams_in_leagues
