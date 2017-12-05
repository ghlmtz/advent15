import re
badstr = ['ab','cd','pq','xy']
s = 0
for line in open('05.in','r').readlines():
	if re.search(r"([aeiou].*){3,}",line):
		for x in badstr:
			if x in line:	break;
		else:
			if re.search(r"(.)\1",line):
				s += 1
print(s)
s = 0
for line in open('05.in','r').readlines():
	if re.search(r"(..).*\1",line):
		if re.search(r"(.).\1",line):
			s += 1
print(s)