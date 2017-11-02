#import football
import team
import player
import test
import test2
import table
import season

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
                                                        
hertha = team.Team("Hertha BSC",
                   "Wappen")

bayern = team.Team("1. FC Bayern Muenchen",
                   "Wappen")

dortmund = team.Team("BVB Dortmund",
                   "Wappen")

duisburg = team.Team("MSV Duisburg",
                   "Wappen")

union = team.Team("1.FC Union Berlin",
                   "Wappen")

leipzig = team.Team("RB Leipzig",
                   "Wappen")

freiburg = team.Team("1. FC Freiburg",
                   "Wappen")

frankfurt = team.Team("Eintracht Frankfurt",
                   "Wappen")

leverkusen = team.Team("Bayer Leverkusen",
                   "Wappen")

hoffenheim = team.Team("TSG Hoffenheim",
                   "Wappen")

bremen = team.Team("Werder Bremen",
                   "Wappen")

kaiserslautern = team.Team("1. FC Kaierslautern",
                   "Wappen")

stuttgart = team.Team("VfB Stuttgart",
                   "Wappen")

duesseldorf = team.Team("Fortuna Duesseldorf",
                   "Wappen")

koeln = team.Team("1. FC Koeln",
                   "Wappen")

hannover = team.Team("Hannover 96",
                   "Wappen")

dresden = team.Team("Dynamo Dresden",
                   "Wappen")

bfc = team.Team("Berliner FC Dynamo",
                   "Wappen")

schalke = team.Team("Schalke 04",
                   "Wappen")

gladbach = team.Team("Borussia Moenchengladbach",
                   "Wappen")

augsburg = team.Team("1. FC Augsburg",
                   "Wappen")

mainz = team.Team("Mainz 05",
                   "Wappen")
                   
wolfsburg = team.Team("VfL Wolfsburg",
                   "Wappen")

hamburg = team.Team("Hamburger SV",
                   "Wappen")

pauli = team.Team("1. FC St. Pauli",
                   "Wappen")
                   
nuernberg = team.Team("1. FC Nuernberg",
                   "Wappen")
                   
teams8 = [hertha, bayern, dortmund, duisburg, union, leipzig, freiburg, frankfurt]
teams18 = [hertha, bayern, dortmund, duisburg, union, leipzig, freiburg, frankfurt, leverkusen, hoffenheim, bremen, kaiserslautern, stuttgart, duesseldorf, koeln, hannover, dresden, bfc]
teams26 = [hertha, bayern, dortmund, duisburg, union, leipzig, freiburg, frankfurt, leverkusen, hoffenheim, bremen, kaiserslautern, stuttgart, duesseldorf, koeln, hannover, dresden, bfc, schalke, gladbach, augsburg, mainz, wolfsburg, hamburg, pauli, nuernberg]

team.set_league(teams26,3)
team.set_league(teams18,2)
team.set_league(teams8,1)

eternal_table = table.Table("Ewige Tabelle")

teams26[0].training_status = True
print teams26[0].training_status
teams26[0].trainer.print_trainer()

season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)
season.season_different_leagues(teams26)
eternal_table = table.print_eternal_table(eternal_table, teams26)

#~ test_teams = [A,B,C,D]
#~ test_teams_2 = [E,F,G,H]
#~ test_teams_3 = [I,J,K,L]
#~ test_teams_4 = [A,B,C,D,E,F,G,H,I,J,K,L]

#~ team.set_league(test_teams,1)
#~ team.set_league(test_teams_2,2)
#~ team.set_league(test_teams_3,3)

#~ eternal_table = table.Table("Ewige Tabelle")

#~ season.season_different_leagues(test_teams_4)

#~ table.print_eternal_table(eternal_table, test_teams)

#~ football.season(test_teams)

#~ table.print_eternal_table(eternal_table, test_teams)

#~ football.set_league(test_teams,1)
#~ football.set_league(test_teams_2,2)
#~ football.set_league(test_teams_3,3)

