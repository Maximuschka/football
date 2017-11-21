import team
import player
import table
import season
import league
import finances
import manager
import menues

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

#~ test_teams = [A,B,C,D]
#~ test_teams_2 = [E,F,G,H]
#~ test_teams_3 = [I,J,K,L]
#~ test_teams_4 = [A,B,C,D,E,F,G,H]

#~ tt = [A,B,C,D,E,F,G,H]

#~ manager_2 = manager.Manager(tt)

#~ team.set_league(test_teams,1)
#~ team.set_league(test_teams_2,2)
#~ team.set_league(test_teams_3,3)

season_1 = season.Season()

#~ eternal_table = table.Table("Ewige Tabelle")

for i in range (0,100):
	menues.start_menu(season_1, i)

	for season_1.matchday in range (0,(len(season_1.leagues[0].teams)*2)-2):
		season.run_season_md(season_1)

eternal_table = table.print_eternal_table(eternal_table, tt)
team.print_teams_by_titles(tt) 

teams32 = team.get_teams_from_text(32)
teams24 = teams32[0:24]
teams16 = teams32[0:16]
teams8 = teams32[0:8]

manager_1 = manager.Manager(teams32)

team.set_league(teams32,4)
team.set_league(teams24,3)
team.set_league(teams16,2)
team.set_league(teams8,1)

season_1 = season.Season(teams32, manager_1)

eternal_table = table.Table("Ewige Tabelle")

for season_1.matchday in range (0,(len(season_1.leagues[0].teams)*2)-2):
	season.season_different_leagues_md(season_1)

eternal_table = table.print_eternal_table(eternal_table, teams32)
team.print_teams_by_titles(teams32) 
#~ season.season_different_leagues(season_1)
#~ eternal_table = table.print_eternal_table(eternal_table, teams32)
#~ team.print_teams_by_titles(teams32)
#~ season.season_different_leagues(season_1)
#~ eternal_table = table.print_eternal_table(eternal_table, teams32)
#~ team.print_teams_by_titles(teams32)
#~ season.season_different_leagues(season_1)
#~ eternal_table = table.print_eternal_table(eternal_table, teams32)
#~ team.print_teams_by_titles(teams32)
#~ season.season_different_leagues(season_1)
#~ eternal_table = table.print_eternal_table(eternal_table, teams32)
#~ team.print_teams_by_titles(teams32)
#~ season.season_different_leagues(season_1)
#~ eternal_table = table.print_eternal_table(eternal_table, teams32)
#~ team.print_teams_by_titles(teams32)
#~ season.season_different_leagues(season_1)
#~ eternal_table = table.print_eternal_table(eternal_table, teams32)
#~ team.print_teams_by_titles(teams32)


#~ test_teams = [A,B,C,D]
#~ test_teams_2 = [E,F,G,H]
#~ test_teams_3 = [I,J,K,L]
#~ test_teams_4 = [A,B,C,D,E,F,G,H,I,J,K,L]

#~ tt = [A,B,C,D,E,F,G,H]

#~ season_2 = season.Season(tt)

#~ team.set_league(test_teams,1)
#~ team.set_league(test_teams_2,2)
#~ team.set_league(test_teams_3,3)

#~ season_2 = season.Season(tt)

#~ season.season_different_leagues(season_2)
#~ eternal_table = table.print_eternal_table(eternal_table, tt)
#~ team.print_teams_by_titles(tt)
#~ season.season_different_leagues(season_2)
#~ eternal_table = table.print_eternal_table(eternal_table, tt)
#~ team.print_teams_by_titles(tt)
#~ season.season_different_leagues(season_2)
#~ eternal_table = table.print_eternal_table(eternal_table, tt)
#~ team.print_teams_by_titles(tt)
#~ season.season_different_leagues(season_2)
#~ eternal_table = table.print_eternal_table(eternal_table, tt)
#~ team.print_teams_by_titles(tt)
#~ season.season_different_leagues(season_2)
#~ eternal_table = table.print_eternal_table(eternal_table, tt)
#~ team.print_teams_by_titles(tt)
#~ season.season_different_leagues(season_2)
#~ eternal_table = table.print_eternal_table(eternal_table, tt)
#~ team.print_teams_by_titles(tt)

#~ teams26[0].training_status = True
#~ print teams26[0].training_status
#~ teams26[0].trainer.print_trainer()
