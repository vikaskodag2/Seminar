import sys
import nltk
from lexicon import Lexicon


lexicon = Lexicon()
lines = lexicon.readlines()

for l in lines:
	print l