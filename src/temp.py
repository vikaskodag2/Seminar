from __future__ import print_function
import subprocess

poscnt = 0
negcnt = 0
neucnt = 0
pos1cnt = 0
neg1cnt = 0
neu1cnt = 0
cnt = 0

f1 = open("Sample/1.txt", 'r')
f2 = open("Sample/2.txt", 'r')
f3 = open("Sample/3.txt", 'r')
f4 = open("Sample/Result.txt", 'w')

for i, line in enumerate(f1) :
	if not line.startswith('\n') :
		if line.startswith('--->') :
			if line.startswith("---> p") :
				pos1cnt += 1
			elif line.startswith("---> n") :
				neg1cnt += 1
			else :
				# print (str(i))
				neu1cnt += 1;
		else :
			line = line.split(' ', 1)[1]
			if '"' in line :
				line = line.replace('"', "")
			cmd = 'python sentiment.py "' + line + '"'
			p = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell = True)
			out, err = p.communicate()
			result = out.split('\n')[0].split(' ', 2)[1]
			print (result[0:1], end=', ')
			if result == "positive" :
				poscnt += 1
			elif result == "negative" :
				negcnt += 1
			else :
				neucnt += 1

print()

for i, line in enumerate(f2) :
	if not line.startswith('\n') :
		if line.startswith('--->') :
			if line.startswith("---> p") :
				pos1cnt += 1
			elif line.startswith("---> n") :
				neg1cnt += 1
			else :
				# print (str(i))
				neu1cnt += 1;
		else :
			line = line.split(' ', 1)[1]
			if '"' in line :
				line = line.replace('"', "")
			cmd = 'python sentiment.py "' + line + '"'
			p = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell = True)
			out, err = p.communicate()
			result = out.split('\n')[0].split(' ', 2)[1]
			print (result[0:1], end=', ')
			if result == "positive" :
				poscnt += 1
			elif result == "negative" :
				negcnt += 1
			else :
				neucnt += 1

print()

for i, line in enumerate(f3) :
	if not line.startswith('\n') :
		if line.startswith('--->') :
			if line.startswith("---> p") :
				pos1cnt += 1
			elif line.startswith("---> n") :
				neg1cnt += 1
			else :
				# print (str(i))
				neu1cnt += 1;
		else :
			line = line.split(' ', 1)[1]
			if '"' in line :
				line = line.replace('"', "")
			cmd = 'python sentiment.py "' + line + '"'
			p = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell = True)
			out, err = p.communicate()
			result = out.split('\n')[0].split(' ', 2)[1]
			print (result[0:1] , end=', ')
			if result == "positive" :
				poscnt += 1
			elif result == "negative" :
				negcnt += 1
			else :
				neucnt += 1

f1.close()
f2.close()
f3.close()

print()
print("Done analyzing. Compiling results!!!")
print()

print("Sentiment analysis on unannotated data from sample results  : ")
print("positive words : " + str(poscnt))
print("negative words : " + str(negcnt))
print("neutral words : " + str(neucnt))
	
print()
print()

print("sample manually annotated results :")
print("positive words : " + str(pos1cnt))
print("negative words : " + str(neg1cnt))
print("neutral words : " + str(neu1cnt))

f4.write("Done analyzing. Compiling results!!!")
f4.write('\n')
f4.write("Sentiment analysis on unannotated data from sample results  : \n")
f4.write("positive words : " + str(poscnt))
f4.write('\n')
f4.write("negative words : " + str(negcnt))
f4.write('\n')
f4.write("neutral words : " + str(neucnt))
f4.write('\n')
f4.write('\n')
f4.write("sample manually annotated results :")
f4.write('\n')
f4.write("positive words : " + str(pos1cnt))
f4.write('\n')
f4.write("negative words : " + str(neg1cnt))
f4.write('\n')
f4.write("neutral words : " + str(neu1cnt))


f4.close()