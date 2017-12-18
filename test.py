from flask import Flask
import season
import manager
import team
import stadium
import table

teams32 = team.get_teams_from_text("teams", 32)
teams24 = teams32[0:24]
teams16 = teams32[0:16]
teams8 = teams32[0:8]

manager_1 = manager.Manager(teams32)

team.set_league(teams32,4)
team.set_league(teams24,3)
team.set_league(teams16,2)
team.set_league(teams8,1)

season_1 = season.Season()

eternal_table = table.Table("Ewige Tabelle")

app = Flask(__name__)

@app.route("/")
def hello():
	print "LALA"
	return teams32[4].name
	return "Hello World!"
