import pickle

def save_season(season):

	dataset = season
	outputFile = 'season.data'
	fw = open(outputFile, 'wb')
	pickle.dump(dataset, fw)
	fw.close()

def load_season():

	inputFile = 'season.data'
	fd = open(inputFile, 'rb')
	dataset = pickle.load(fd)

	return dataset
