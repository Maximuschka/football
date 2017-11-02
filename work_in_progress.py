import team
#import football
from operator import itemgetter, attrgetter, methodcaller
import csv

def write_table_to_csv(teams):
	
	"""This function is supposed to write current table to a text file"""
	
	teams_sorted_diff = sorted(teams, key=lambda team:team.get_diff_goals(), reverse=True)
	teams_sorted_points = sorted(teams_sorted_diff, key=attrgetter('points'), reverse=True)
	
	thefile = open('table2.txt','w')
	for item in teams_sorted_points:
		thefile.write("%s\n" % item)
	#~ with open('table.csv','wb') as myfile:
		#~ wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		#~ wr.writerow(teams_sorted_points)

def read_table_from_csv():

	"""This functio is supposed to read the current table from a text file
	"""

	teams = open("table2.txt",'r').read().splitlines()
	print(teams)
	print(teams[0].name)

	#~ with open('table.csv', 'rb') as f:
		#~ reader = csv.reader(f)
		#~ teams_sorted = list(reader)
	#~ print(teams_sorted)

	#~ count = len(teams)
	#~ i = 0
    
	#~ while(i < count):
		#~ print(str(i+1) + ". - " + teams_sorted_points[i].name + "  " + str(teams_sorted_points[i].games_played) + "   "+ str(teams_sorted_points[i].points) + "   " + str(teams_sorted_points[i].get_diff_goals()) + "  " + str(int(teams_sorted_points[i].get_efficiency())) + "   Staerke: " + str(teams_sorted_points[i].strength)+ "   Taktik: " + str(teams_sorted_points[i].tactic)+ "   Moral: " + str(teams_sorted_points[i].moral))
		#~ i = i+1


		#~ Bislang schribet die Funktion nur die Speicherorte in ein CSV. 
		#~ Ist das ausreichend fuer das calling?!
