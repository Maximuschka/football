import game

class Matchday:
	
	"""Class to store the results of a single match day"""

	def __init__(self):
		self.matches = []
		
	def add_match(self, game):
		
		"""Adding a single gameto a matchday"""
		
		self.matches.append(game)
