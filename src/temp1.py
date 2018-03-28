from __future__ import print_function
import subprocess


poscnt = 0
negcnt = 0
neucnt = 0

filename = "Sample/4.txt"
fname = "Sample/Result1.txt"

f1 = open(filename, 'r')
f2 = open(fname, 'w')

cnt = 1
for line in f1 :
	if not "http" in line :
		if not ".com" in line :
			if '"' in line :
				line = line.replace('"', "")
			cmd = 'python sentiment.py "' + line + '"'
			p = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell = True)
			out, err = p.communicate()
			result = out.split('\n')[0].split(' ', 2)[1]
			print (str(cnt) + " : " + result)
			if result == "positive" :
				poscnt += 1
			elif result == "negative" :
				negcnt += 1
			else :
				neucnt += 1
			cnt += 1


print("Sentiment analysis on unannotated data from twitter, results  : ")
print("positive words : " + str(poscnt))
print("negative words : " + str(negcnt))
print("neutral words : " + str(neucnt))

f2.write("Sentiment analysis on unannotated data from twitter, results  : \n")
f2.write("positive words : " + str(poscnt))
f2.write('\n')
f2.write("negtive words : " + str(negcnt))
f2.write('\n')
f2.write("neutral words : " + str(neucnt))
f2.write('\n')

f1.close()
f2.close()