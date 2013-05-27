import re

DATABASE = "igures.sqlite"
BATCH_SIZE = 10000

PATTERNS = [
	"{verb} {adv}",
	"{adv} {verb} the {adj} {noun}",
	"{adj} {noun}"
]
FREQUENCY_THRESHOLD = 55000

PATTERN_PLACEHOLDER_EXP = re.compile("{(\w+)}")
