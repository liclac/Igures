class Word(object):
	def __init__(self, freq, class_, word):
		self.freq = int(freq)
		self.class_ = class_
		self.word = word
	def __str__(self):
		return "[%d] %s: %s" % (self.freq, self.class_, self.word)

class WordSource(object):
	def iterwords(self):
		pass

