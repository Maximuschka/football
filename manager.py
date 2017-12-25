import random
import team

class Manager:

	def __init__(self):
		#~ self.name = set_manager_name()
		#~ self.team = set_manager_team(self, teams)
		self.name = ""
		self.team = ""
		
	def set_training_status(self):
		check = raw_input("Shall your team "+ self.team.name +" be trained? " )
		
		if check in ("Yes", "yes"):
			self.team.training_status = True
		
		else:
			self.team.training_status = False

	def set_name(self, name):
		self.name = name

	def set_team(self, team):
		self.team = team

def set_manager_name():
	name = raw_input("What's your name? Input: ")
	print ""
	return name
	
def set_manager_team(manager, teams):
	print "Dear " + manager.name + ", in a next step, please define which team you would like to play:"
	team.print_teams(teams)
	team_id = input("Team ID: ")
	print ""
	return teams[team_id-1]

