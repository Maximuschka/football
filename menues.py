import manager
import season
import team
import table

A = team.Team("A",
                   "Wappen")

B = team.Team("B",
                   "Wappen")

C = team.Team("C",
                   "Wappen")

D = team.Team("D",
                   "Wappen")
 
E = team.Team("E",
                   "Wappen")

F = team.Team("F",
                   "Wappen")

G = team.Team("G",
                   "Wappen")

H = team.Team("H",
                   "Wappen")
                   
I = team.Team("I",
                   "Wappen")

J = team.Team("J",
                   "Wappen")

K = team.Team("K",
                   "Wappen")

L = team.Team("L",
                   "Wappen")

def start_menu(season_2, count):
	
	if count == 0:
		
		print "This is the first season you are playing. You will have to make some choices."
		print ""
		
		test_teams = [A,B,C,D]
		test_teams_2 = [E,F,G,H]
		test_teams_3 = [I,J,K,L]
		test_teams_4 = [A,B,C,D,E,F,G,H]

		tt = [A,B,C,D,E,F,G,H]

		manager_2 = manager.Manager(tt)

		team.set_league(test_teams,1)
		team.set_league(test_teams_2,2)
		team.set_league(test_teams_3,3)
		
		
		season_2.add_teams(tt)
		season_2.add_manager(manager_2)
		
		return season
		
	else:
	
		print ""
		check = raw_input("Season " + str(season_2.year) + " is over. Do you want to start the next season? (Yes / No)")
		
		if check in ("Yes", "yes"):
			print ""
			return
		
		else:
			print ""
			quit()

def run_mainmenu(season):
	print "Main menu"
	print ""
	print "Season " + str(season.year)
	print ""
	print "Team Manager: " + season.manager.name
	print "Team: " + season.manager.team.name
	print ""
	print "1 - Players"
	print "2 - Finances"
	print "3 - Stadium"
	print "4 - Training"
	print "5 - Next game"
	print "6 - Table"
	print "7 - Top Scorers"
	print "8 - Eternal Table"
	print "9 - Exit"
	print("_____________________________________________")
	
	menu_id = raw_input("Please choose which menu to access. Menu ID: ")
	print ""
	try:
		menu_id_int = int(menu_id)
		if menu_id_int == 1:
			run_players_menu(season)

		elif menu_id_int == 2:
			run_finances_menu(season)

		elif menu_id_int == 3:
			run_stadium_menu()

		elif menu_id_int == 4:
			run_training_menu()

		elif menu_id_int == 5:
			run_next_game()

		elif menu_id_int == 7:
			run_top_scorers(season)

		elif menu_id_int == 8:
			run_eternal_table(season)

	except ValueError:
		run_next_game()

def run_players_menu(season):
	season.manager.team.print_players()
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season)
	
def run_finances_menu(season):
	season.manager.team.finances.print_finances()
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season)

def run_next_game():
	return

def run_top_scorers(season):
	print "There are " + str(len(season.leagues)) + " leagues currently." 
	league_id = input("Which leagues top scorer shall be displayed?")
	
	print ""
	print "Top scorers of league " + str(season.leagues[league_id].teams[0].league)
	print ""

	team.print_top_scorers(season.leagues[league_id].teams)
	
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season)

def run_eternal_table(season):
	print ""
	print "Eternal table:"
	print ""
	table.print_table(season.et.teams)
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season)
