import random
import team

class Manager:

	def __init__(self,teams):
		self.name = set_manager_name()
		self.team = set_manager_team(self, teams)

	def set_training_status(self):
		check = raw_input("Shall your team "+ self.team.name +" be trained? " )
		
		if check in ("Yes", "yes"):
			self.team.training_status = True
		
		else:
			self.team.training_status = False

	#~ def set_trained_feature(self):
		#~ print "Which feature would you like to train:"
		#~ print "0 - Offense"
		#~ print "1 - Defense"
		#~ print "2 - Power"
		#~ print "3 - Endurance"
		#~ feature = input("Input: ")
		
		

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

