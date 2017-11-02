import team
import football
from operator import itemgetter, attrgetter, methodcaller
import csv
import copy

def eternal_table(eternal_teams, teams):

	teams_1 = team.get_teams_from_league(teams,1)
	
	for i in range (0,len(teams_1)):
		if team.eq_name(teams_1[i], eternal_teams) == True:
			break
		elif team.eq_name(teams_1[i], eternal_teams) == False:
			dummy_team = copy.deepcopy(teams_1[i])
		
			dummy_team.games_played = 0
			dummy_team.points = 0
			dummy_team.scored_goals = 0
			dummy_team.received_goals = 0
			dummy_team.attempts = 0
			
			eternal_teams.append(dummy_team)
		else:
			print ("Error")
			break
			
	for i in range (0, len(teams_1)):
		for j in range (0, len(eternal_teams)):
			if teams_1[i].name == eternal_teams[j].name:
				eternal_teams[j].games_played = eternal_teams[j].games_played + teams_1[i].games_played
				eternal_teams[j].points = eternal_teams[j].points + teams_1[i].points 
				eternal_teams[j].scored_goals = eternal_teams[j].scored_goals + teams_1[i].scored_goals
				eternal_teams[j].received_goals = eternal_teams[j].received_goals + teams_1[i].received_goals
				eternal_teams[j].attempts = eternal_teams[j].attempts + teams_1[i].attempts
	
	print("")
	print("Ewige Tabelle")
	print("")
	football.print_table(eternal_teams)
	print("_____________________________________________")
	raw_input("Press Enter to continue...")
	print("")

	return eternal_teams
