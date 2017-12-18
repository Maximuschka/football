import manager
import season
import team
import table
import memory 
import trainer
import player
import stadium
import test2


def start_menu():
	
	for i in range (0,100):

		if i == 0:

			print "Max's Football Manager 1987 Deluxe"
			print ""
			print "1 - New Game"
			print "2 - Load Game"
			print ""
			user_input = raw_input()
			print ""
			
			try:
			
				user_input = int(user_input)

				if user_input == 2:
					season_1 = memory.load_season()
					print season_1.year
					print season_1.matchday

				else:
					season_1 = season.Season()

					teams32 = team.get_teams_from_text("teams",32)
					teams24 = teams32[0:24]
					teams16 = teams32[0:16]
					teams8 = teams32[0:8]
					
					manager_1 = manager.Manager(teams32)
					
					team.set_league(teams32,4)
					team.set_league(teams24,3)
					team.set_league(teams16,2)
					team.set_league(teams8,1)

					season_1.add_teams(teams32)
					season_1.add_manager(manager_1)

					#~ test_teams8 = team.get_teams_from_text("test_teams",8)
					#~ test_teams4 = test_teams8[0:4]

					#~ team.set_league(test_teams8,2)
					#~ team.set_league(test_teams4,1)
					
					#~ manager_2 = manager.Manager(test_teams8)
					
					#~ season_1.add_teams(test_teams8)
					#~ season_1.add_manager(manager_2)

			except ValueError:
				print "Input error!"
				print ""
				start_menu()

		else:
			print ""
			check = raw_input("Season " + str(season_1.year) + " is over. Do you want to start the next season? (Yes / No)")
			
			if check in ("No", "no"):
				print ""
				quit()

			else:
				print ""

		while season_1.matchday < (len(season_1.leagues[0].teams)*2)-2:
			if season_1.matchday == 0:
				season_1 = season.new_season(season_1)
			#~ season.new_matchday(season_1)
			run_mainmenu(season_1)

def run_mainmenu(season_1):
	
	print("_____________________________________________")
	print "Main menu"
	print ""
	print "Season " + str(season_1.year) + " - Matchday: " + str(season_1.matchday + 1)
	print ""
	print "Team Manager: " + season_1.manager.name
	print "Team: " + season_1.manager.team.name
	print "Strength: " + str(int(season_1.manager.team.strength))
	print "League: " + str(season_1.manager.team.league) + "."
	print "Injured player: " + str(season_1.manager.team.count_injured_players())
	print ""
	print "1  - Next game"
	print "2  - Players"
	print "3  - Finances"
	print "4  - Stadium"
	print "5  - Training"
	print "6  - Transfers"
	print "7  - Table"
	print "8  - Top Scorers"
	print "9  - Eternal Table"
	print "10 - Record winners"
	print "11 - Preferences"
	print ""
	menu_id = raw_input("Please choose which menu to access. Menu ID: ")
	print ""
	try:
		menu_id_int = int(menu_id)

		if menu_id_int == 1:
			run_next_game(season_1)

		elif menu_id_int == 2:
			run_players_menu(season_1)

		elif menu_id_int == 3:
			run_finances_menu(season_1)

		elif menu_id_int == 4:
			run_stadium_menu(season_1)

		elif menu_id_int == 5:
			run_training_menu(season_1)

		elif menu_id_int == 6:
			run_transfers(season_1)

		elif menu_id_int == 7:
			run_table(season_1)

		elif menu_id_int == 8:
			run_top_scorers(season_1)

		elif menu_id_int == 9:
			run_eternal_table(season_1)

		elif menu_id_int == 10:
			run_record_winners(season_1)

		elif menu_id_int == 10:
			run_preferences(season_1)

		elif menu_id_int == 11:
			run_preferences(season_1)

	except ValueError:
		run_next_game(season_1)

def run_next_game(season_1):
	#~ condition = season.condition_md(season_1)
	#~ if condition == False:
		#~ print "Returning to main menu"
		#~ run_mainmenu(season_1)
	#~ elif condition == True:
	season.run_season_md(season_1)

def run_players_menu(season_1):
	print("_____________________________________________")
	print "Player menu"
	print ""
	season_1.manager.team.print_players()
	print ""
	check = raw_input("Would you like substitute players?")

	if check in ("Yes", "yes"):
		season_1.manager.team.swap_player()

	print raw_input("Press Enter to return to Main Menu...")
	#~ return
	run_mainmenu(season_1)
	
def run_finances_menu(season_1):
	print("_____________________________________________")
	print "Finances menu"
	print ""
	season_1.manager.team.finances.print_finances(season_1)
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season_1)

def run_stadium_menu(season_1):

	md = season_1.matchday
	s = season_1.get_season_count()

	print("_____________________________________________")
	print "Stadium menu"
	print ""
	season_1.manager.team.stadium.print_stadium_info()
	
	print ""
	print "1  - Change ticket prize"
	print "2  - Increase capacity"
	print "3  - Return to main menu"
	print ""
	menu_id = raw_input("Please choose which menu to access. Menu ID: ")

	try:
		menu_id_int = int(menu_id)

		if menu_id_int == 1:
			season_1.manager.team.stadium.request_new_ticket_prize()

		elif menu_id_int == 2:
			stadium.run_stadium_construction(season_1)
		
		elif menu_id_int == 3:
			run_mainmenu(season_1)

	except ValueError:
		print "Input error!"
		print ""
		run_stadium_menu(season_1)

	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season_1)

def run_training_menu(season_1):
	print("_____________________________________________")
	print "Training menu"
	print ""
	trainer.print_trainers(season_1.manager.team.trainers)
	print ""
	
	feature = 0
	
	user_input = raw_input("Shall your team "+ season_1.manager.team.name +" be trained? " )
	
	if user_input in ("Yes", "yes"):
		status = True
		print ""
		print "Following features can be trained: "
		print "1 - Offense"
		print "2 - Defense"
		print "3 - Power"
		print "4 - Endurance"
		print ""
		feature = input("Which feature shall be trained?") - 1
	else:
		status = False
	
	season_1.manager.team.set_training_status(status)
	season_1.manager.team.set_trained_feature(feature)
	
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season_1)

def run_transfers(season_1):
	print("_____________________________________________")
	print "Transfer menu"
	print ""

	print ""
	print "You have following transfer options: "
	print "1 - Sell player"
	print "2 - Buy player"
	print "3 - Sell trainer"
	print "4 - Buy trainer"
	print ""
	user_input = raw_input("What would you like to do?")

	print ""
	try:
		user_input = int(user_input)
		if user_input == 1:
			team.run_sell_player(season_1)

		elif user_input == 2:
			team.run_buy_player(season_1)

		elif user_input == 3:
			team.run_sell_trainer(season_1)

		elif user_input == 4:
			team.run_buy_trainer(season_1)

	except ValueError:
		run_mainmenu(season_1)

	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season_1)

def run_top_scorers(season_1):
	print("_____________________________________________")
	print "Top scorers"
	print ""
	print "There are " + str(len(season_1.leagues)) + " leagues currently." 
	league_id = input("Which leagues top scorer shall be displayed?") -1
	
	print ""
	print "Top scorers of league " + str(season_1.leagues[league_id].teams[0].league)
	print ""

	team.print_top_scorers(season_1.leagues[league_id].teams)
	
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season_1)

def run_table(season_1):
	print("_____________________________________________")
	print "Table"
	print ""
	print "There are " + str(len(season_1.leagues)) + " leagues currently." 
	league_id = input("Which league's table shall be displayed?") -1
	
	print ""
	print "Table of league " + str(season_1.leagues[league_id].teams[0].league)
	print ""

	table.print_table(season_1.leagues[league_id].teams)
	
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season_1)

def run_eternal_table(season_1):
	print("_____________________________________________")
	print "Eternal table:"
	print ""
	table.print_table(season_1.et.teams)
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season_1)

def run_record_winners(season_1):
	print("_____________________________________________")
	print "Record winners:"
	print ""
	
	team.print_teams_by_titles(season.get_list_of_teams_from_season(season_1))
	
	print ""
	print raw_input("Press Enter to return to Main Menu...")
	run_mainmenu(season_1)

def run_preferences(season_1):
	print("_____________________________________________")
	print "Preferences:"
	print ""
	print "1  - Load/Save"
	print "2  - Exit"
	print ""
	menu_id = raw_input("Please choose which menu to access. Menu ID: ")
	print ""
	try:
		menu_id_int = int(menu_id)

		if menu_id_int == 1:
			season_1 = run_memory(season_1)

		elif menu_id_int == 2:
			quit()

	except ValueError:
		run_next_game(season_1)

def run_memory(season_1):
	print("_____________________________________________")
	print "Load/Save:"
	print ""
	print "You have following transfer options: "
	print "1 - Load game"
	print "2 - Save game"
	print "3 - Back to Main Menu"
	print ""
	user_input = raw_input("What would you like to do? " )
	print ""

	try:
		user_input = int(user_input)
		if user_input == 1:
			season_1 = memory.load_season()

			print ""
			print "Data is loaded."
			print ""
			print raw_input("Press Enter to return to Main Menu...")
			run_mainmenu(season_1)

		elif user_input == 2:
			memory.save_season(season_1)

			print ""
			print "Data is stored."
			print ""
			print raw_input("Press Enter to return to Main Menu...")
			run_mainmenu(season_1)

	except ValueError:
		run_mainmenu(season_1)

