import team
import copy


class Table:

	def __init__(self, name):
		self.name = name
		self.teams = []
	
	def add_team(self,team):
		self.teams.append(team)

	def compare_and_add(self,teams):
		for i in range (0,len(teams)):
			if team.eq_name(teams[i], self.teams) == False:
				dummy_team = copy.deepcopy(teams[i])
			
				dummy_team.games_played = 0
				dummy_team.points = 0
				dummy_team.scored_goals = 0
				dummy_team.received_goals = 0
				dummy_team.attempts = 0
				
				self.teams.append(dummy_team)

def print_table(teams):

	"""Prints the table
	Input: List of instances of Class Team
	Output: Printed table"""

	teams_sorted = team.sort_teams(teams)

	count = len(teams_sorted)
	i = 0

	print "{:2}#  | {:19.19}Team |{:2}S | {:2}P| {:1}TD | {:1}E| {:1}F| {:1}T | {:1}M".format("","","","","","","","","")
	while(i < count):
		print "{pos:3}. | {tname:23.23} |{tgp:3} | {tp:3}| {tdiff:3} | {teff:2}| {ts:2}| {tt:2} | {tm:2}".format(pos = i+1,
																												tname = teams_sorted[i].name,
																												tgp = teams_sorted[i].games_played, 
																												tp = teams_sorted[i].points, 
																												tdiff = teams_sorted[i].get_diff_goals(), 
																												teff = int(teams_sorted[i].get_efficiency()), 
																												ts = int(teams_sorted[i].strength), 
																												tt = teams_sorted[i].tactic, 
																												tm = teams_sorted[i].moral)
		#~ print(str(i+1) + ". - " + teams_sorted[i].name + "  " + str(teams_sorted[i].games_played) + "   "+ str(teams_sorted[i].points) + "   " + str(teams_sorted[i].get_diff_goals()) + "  " + str(int(teams_sorted[i].get_efficiency())) + "   Staerke: " + str(teams_sorted[i].strength)+ "   Taktik: " + str(teams_sorted[i].tactic)+ "   Moral: " + str(teams_sorted[i].moral))
		i = i+1

def get_table_for_gui(teams):
	
	"""
	returns a list of strings to print table with appJar
	Input: List of instances of Class Team
	Output: List of strings, including all important information to print
	"""

	table_for_gui = ""
	teams_sorted = team.sort_teams(teams)

	#~ table_for_gui += "arsch"
	table_for_gui += ("{:2}#  | {:^26}Team |{:2}S | {:2}P| {:1}TD | {:1}E| {:1}F| {:1}T | {:1}M".format("","","","","","","","",""))
	table_for_gui += "\n"
	for i in range(len(teams_sorted)):
		table_for_gui += "{pos:3}. | {tname:30}|{tgp:3}| {tp:3}| {tdiff:3}| {teff:2}| {ts:2}| {tt:2} | {tm:2}".format(pos = i+1,
																												tname = teams_sorted[i].name,
																												tgp = teams_sorted[i].games_played, 
																												tp = teams_sorted[i].points, 
																												tdiff = teams_sorted[i].get_diff_goals(), 
																												teff = int(teams_sorted[i].get_efficiency()), 
																												ts = int(teams_sorted[i].strength), 
																												tt = teams_sorted[i].tactic, 
																												tm = teams_sorted[i].moral)
																												
		table_for_gui += "\n"

	return table_for_gui

def update_eternal_table(eternal_t, teams):

	teams_1 = team.get_teams_from_league(teams,1)
	
	eternal_t.compare_and_add(teams_1)
	
	for i in range (0, len(teams_1)):
		for j in range (0, len(eternal_t.teams)):
			if teams_1[i].name == eternal_t.teams[j].name:
				eternal_t.teams[j].games_played = eternal_t.teams[j].games_played + teams_1[i].games_played
				eternal_t.teams[j].points = eternal_t.teams[j].points + teams_1[i].points 
				eternal_t.teams[j].scored_goals = eternal_t.teams[j].scored_goals + teams_1[i].scored_goals
				eternal_t.teams[j].received_goals = eternal_t.teams[j].received_goals + teams_1[i].received_goals
				eternal_t.teams[j].attempts = eternal_t.teams[j].attempts + teams_1[i].attempts

	print("")
	print("Ewige Tabelle")
	print("")
	print_table(eternal_t.teams)
	print("_____________________________________________")
	raw_input("Press Enter to continue...")
	print("")
	
	return eternal_t



#~ def update_eternal_table(eternal_table, teams):
	
