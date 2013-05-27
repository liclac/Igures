import os
from models import Word, WordSource

class WordNetDict(WordSource):
	'''A source that reads a WordNet database.'''
	classes = ['adj', 'adv', 'noun', 'verb']
	files = []
	
	def __init__(self, path):
		self.path = path
		for class_ in self.classes:
			self.files.insert(0,
				(
					class_,
					open(os.path.join(self.path, 'data.%s' % class_))
				)
			)
	
	def iterwords(self):
		for class_ in self.classes:
			path = os.path.join(self.path, 'data.%s' % class_)
			with open(path) as f:
				while True:
					line = f.readline()
					while line.startswith("  "):
						line = f.readline()
					if not line:
						break
					
					parts = line.split(' ')
					yield Word(parts[0], class_, parts[4])
					
