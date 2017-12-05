i = open('01.in','r').read().rstrip()
print(i.count('(')-i.count(')'))	# Part 1
s = 0
for N,char in enumerate(i):
	s += 1 if char == '(' else -1
	if s < 0:	print(N+1); break	# Part 2