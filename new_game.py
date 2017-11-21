import team
import player
import table
import season
import league
import finances
import manager
import menues

season_1 = season.Season()

for i in range (0,100):
	menues.start_menu(season_1, i)

	for season_1.matchday in range (0,(len(season_1.leagues[0].teams)*2)-2):
		season.run_season_md(season_1)

team.print_teams_by_titles(tt)
