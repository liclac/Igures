import os
import sqlite3

class Igures(object):
	'''Main class for Igures.
	This is the class you most likely want to talk to.'''
	db = None
	
	def __init__(self, db_path, source = None):
		'''Create a new Igures, using the specific database and optional source.
		If the database doesn't exist, and source is specified, it will be 
		created and populated by words pulled from the source.'''
		
		if source:
			os.remove(db_path)
			self._db_connect(db_path)
			self._db_setup()
			self._import(source)
		elif os.path.exists(db_path):
			self._db_connect(db_path)
		else:
			raise NoDatabaseException()
	
	def _db_connect(self, db_path):
		self.db = sqlite3.connect(db_path)
	
	def _db_setup(self):
		print("Setting up a new database...")
		self.db.execute('''
			CREATE TABLE words (
				id INTEGER PRIMARY KEY,
				freq INTEGER,
				class TEXT,
				word TEXT
			)
		''')
	
	def _import(self, source):
		print("Importing data...")
		import time
		batch_counter = 0
		words_imported = 0
		
		t0 = time.time()
		cursor = self.db.cursor()
		for word in source.iterwords():
			cursor.execute("INSERT INTO words (freq, class, word) VALUES (?, ?, ?)",
				(word.freq, word.class_, word.word))
			batch_counter = batch_counter + 1
			words_imported = words_imported + 1
			if batch_counter >= config.BATCH_SIZE:
				print("%d Words imported, committing..." % words_imported)
				self.db.commit()
				batch_counter = 0
		self.db.commit()
		t1 = time.time()
		
		t = t1 - t0
		print("Imported %d words in %s seconds" % (words_imported, t))

class NoDatabaseException(Exception):
	pass

if __name__ == '__main__':
	import argparse
	from wordnet import WordNetDict
	import config
	
	parser = argparse.ArgumentParser(description="Generates random sentences.")
	parser.add_argument('--init-wordnet', metavar="PATH", dest='wordnet_path', help="Initializes the database, using a WordNet 3.1 'dict' directory as a source. You can obtain a copy of WordNet at http://wordnet.princeton.edu/wordnet/download/.")
	args = parser.parse_args()
	
	source = None
	if args.wordnet_path:
		source = WordNetDict(args.wordnet_path)
		#for w in source.iterwords():
		#	print(w)
	
	igures = Igures(config.DATABASE, source)

