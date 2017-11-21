import manager
import season
import team
import table

def start_menu(season_1, count):
	
	if count == 0:
		
		print "This is the first season you are playing. You will have to make some choices."
		print ""
		
		#~ teams32 = team.get_teams_from_text("teams",32)
		#~ teams24 = teams32[0:24]
		#~ teams16 = teams32[0:16]
		#~ teams8 = teams32[0:8]
		
		#~ manager_1 = manager.Manager(teams32)
		
		#~ team.set_league(teams32,4)
		#~ team.set_league(teams24,3)
		#~ team.set_league(teams16,2)
		#~ team.set_league(teams8,1)

		#~ season_1.add_teams(teams32)
		#~ season_1.add_manager(manager_1)
		
		#~ return season_1

		test_teams8 = team.get_teams_from_text("test_teams",8)
		test_teams4 = test_teams8[0:4]

		team.set_league(test_teams8,2)
		team.set_league(test_teams4,1)
		
		manager_2 = manager.Manager(test_teams8)
		
		season_1.add_teams(test_teams8)
		season_1.add_manager(manager_2)
		
		return season_1
		
	else:
	
		print ""
		check = raw_input("Season " + str(season_1.year) + " is over. Do you want to start the next season? (Yes / No)")
		
		if check in ("Yes", "yes"):
			print ""
			return
		
		else:
			print ""
			quit()

def run_mainmenu(season):
	print("_____________________________________________")
	print "Main menu"
	print ""
	print "Season " + str(season.year)
	print ""
	print "Team Manager: " + season.manager.name
	print "Team: " + season.manager.team.name
	print "League: " + str(season.manager.team.league) + "."
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
	print ""
	menu_id = raw_input("Please choose which menu to access. Menu ID: ")
	print ""
	try:
		menu_id_int = int(menu_id)
		if menu_id_int == 1:
			run_players_menu(season)

		elif menu_id_int == 2:
			run_finances_menu(season)

		elif menu_id_int == 3:
			run_stadium_menu(season)

		elif menu_id_int == 4:
			run_training_menu(season)

		elif menu_id_int == 5:
			run_next_game()

		elif menu_id_int == 7:
			run_top_scorers(season)

		elif menu_id_int == 8:
			run_eternal_table(season)

	except ValueError:
		run_next_game()

def run_players_menu(season):
	print("_____________________________________________")
	print "Player menu"
	print ""
	season.manager.team.print_players()
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season)
	
def run_finances_menu(season):
	print("_____________________________________________")
	print "Finances menu"
	print ""
	season.manager.team.finances.print_finances()
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season)

def run_stadium_menu(season):
	print("_____________________________________________")
	print "Stadium menu"
	print ""
	season.manager.team.stadium.print_stadium_info()
	
	check = raw_input("Would you like to change the ticket prize?")

	if check in ("Yes", "yes"):
		season.manager.team.stadium.request_new_ticket_prize()
	
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season)

def run_training_menu(season):
	print("_____________________________________________")
	print "Training menu"
	print ""
	season.manager.team.trainer.print_trainer()

	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season)

def run_next_game():
	return

def run_top_scorers(season):
	print("_____________________________________________")
	print "Top scorers"
	print ""
	print "There are " + str(len(season.leagues)) + " leagues currently." 
	league_id = input("Which leagues top scorer shall be displayed?") -1
	
	print ""
	print "Top scorers of league " + str(season.leagues[league_id].teams[0].league)
	print ""

	team.print_top_scorers(season.leagues[league_id].teams)
	
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season)

def run_eternal_table(season):
	print("_____________________________________________")
	print "Eternal table:"
	print ""
	table.print_table(season.et.teams)
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season)
