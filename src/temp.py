import re
from nltk.corpus import wordnet

word = "good"
check = re.sub(r'\!|;|\||\.|\?|,|:|"|\)|\(','',word)

if(wordnet.synsets(check)):
	if(word == check):
		print(word)
	else :
		print(check + "".join(set(word[len(check):])))
else:
	print("gg")