class Word(object):
	'''Represents a single word.'''	
	
	def __init__(self, freq, class_, word):
		self.freq = int(freq)
		self.class_ = class_
		self.word = word
	
	def __str__(self):
		return "[%d] %s: %s" % (self.freq, self.class_, self.word)

class WordSource(object):
	'''Abstract class for a source of words, used when populating the database.'''
	
	def iterwords(self):
		'''This function should iterate over every word available and yield it,
		preferrably not killing the host machine with RAM and CPU usage in the
		process.'''
		pass

