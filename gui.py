from operator import itemgetter, attrgetter, methodcaller
import manager
import season
import team
import table

from appJar import gui

season_1 = season.Season()

teams32 = team.get_teams_from_text("teams",32)
teams24 = teams32[0:24]
teams16 = teams32[0:16]
teams8 = teams32[0:8]

manager_1 = manager.Manager()
team_name_1 = ""

team.set_league(teams32,4)
team.set_league(teams24,3)
team.set_league(teams16,2)
team.set_league(teams8,1)

season_1.add_teams(teams32)
season_1.add_manager(manager_1)

teams32_names = team.get_team_names_in_list(teams32)

def press1(win):
	if win == "Cancel":
		app.stop()

	else:
		app.showSubWindow(win)

def press2(button):
	if button == "Return":
		app.hideSubWindow("New Game")

	else:
		manager_name = app.getEntry("Your name: ")
		team_name_1 = app.getOptionBox("teams")
		manager_team = team.get_team_from_list(teams32, team_name_1)
		manager_1.set_name(manager_name)
		manager_1.set_team(manager_team)
		app.hideSubWindow("New Game")
		app.showSubWindow("Main Menu")

def press3(win):

	global season_1

	if win == "Exit":
		app.hideSubWindow("Main Menu")

	elif win == "Start Matchday":
		print season_1.matchday
		if season_1.matchday == 0:
			season_1 = season.new_season(season_1)
		season.run_season_md(season_1)

	else:
		app.showSubWindow(win)
	
	#~ elif button == "Table":
		#~ app.hideSubWindow("Main Menu")
		#~ app.showSubWindow("Table")
		#~ league = manager_1.team.league
		#~ table.print_table(season_1.leagues[league-1].teams)

	#~ elif button == "Eternal Table":
		#~ table.print_eternal_table(eternal_table, teams32)

	#~ elif button == "Top Scorers":
		#~ league = manager_1.team.league
		#~ team.print_top_scorers(season_1.leagues[league-1].teams)

	#~ elif button == "Team":
		#~ manager_1.team.print_players() 

	#~ elif button == "Start Matchday":
		#~ season.season_different_leagues_md(season_1)

	#~ else:
		#~ print "Under Construction"

def press4(button):
	if button == "MainM1":
		app.showSubWindow("Main Menu")
		app.hideSubWindow("Table")

def press5(button):
	if button == "MainM2":
		app.showSubWindow("Main Menu")
		app.hideSubWindow("Eternal Table")

def leagueChoiceButton(button):
	if button == "One":
		printTable(0)
	elif button == "Two":
		printTable(1)
	elif button == "Three":
		printTable(2)
	elif button == "Four":
		printTable(3)

def printTable(league):
	gui_teams = table.get_table_for_gui(season_1.leagues[league].teams)
	app.setTextAreaState("current_table", "normal")
	app.clearTextArea("current_table", callFunction=True)
	app.setTextArea("current_table", gui_teams, end=True, callFunction=True)
	app.setTextAreaState("current_table", "disabled")

app = gui()

#Start menu
app.setGeometry(300,300)

app.addLabel("title", "Football game")
app.setLabelBg("title", "red")

app.addButton("New Game", press1)
app.addButton("Load Game", press1)
app.addButton("Cancel", press1)

#New Game menu
app.startSubWindow("New Game", modal=True)
app.setGeometry(300,300)
app.addLabel("l1", "New Game")
app.addLabelEntry("Your name: ")
app.addOptionBox("teams", teams32_names)
app.addButtons(["Start Game", "Return"], press2)
app.stopSubWindow()

#Load Game menu
app.startSubWindow("Load Game", modal=True)
app.setGeometry(300,300)
app.addLabel("l2", "Load Game")
app.stopSubWindow()

#Main menu
app.startSubWindow("Main Menu", modal=True)
app.setGeometry(300,300)
app.addLabel("l3", "Main Menu")
app.addButton("Table", press3)
#~ app.addButton("Eternal Table", press3)
#~ app.addButton("Top Scorers", press3)
#~ app.addButton("Team", press3)
#~ app.addButton("Stadium", press3)
#~ app.addButton("Finances", press3)
#~ app.addButton("Training", press3)
app.addButton("Start Matchday", press3)
#~ app.addButton("Save Game", press3)
#~ app.addButton("Exit", press3)
app.stopSubWindow()

#Table menu
app.startSubWindow("Table", modal=True)
app.setGeometry(700,300)
app.addLabel("l4", "Table")
app.addTextArea("current_table")
app.setTextAreaWidth("current_table", 50)
app.setTextAreaHeight("current_table", 15)

app.addButtons(["One", "Two","Three","Four"],leagueChoiceButton)
app.addNamedButton("Back to Main Menu","MainM1", press4)
app.stopSubWindow()

#Eternal Table menu
app.startSubWindow("Eternal Table", modal=True)
app.setGeometry(700,300)
app.addLabel("l5", "Table")
app.addTextArea("eternal_table")
app.setTextAreaWidth("eternal_table", 70)
app.setTextAreaHeight("eternal_table", 15)
app.addNamedButton("Back to Main Menu", "MainM2", press5)
app.stopSubWindow()

app.go()
