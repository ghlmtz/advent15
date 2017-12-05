import re, itertools
dist = {}
cities = set()
for line in open('09.in','r').readlines():
	m = re.match('(\w+) to (\w+) = (\d+)',line)
	to,fro,d = m.group(1,2,3)
	dist[(to,fro)] = int(d)
	dist[(fro,to)] = int(d)
	cities.add(to)
	cities.add(fro)
perms = list(itertools.permutations(cities,len(cities)))
dist_sum = []
for perm in perms:
	s = 0
	for x in range(len(perm)-1):
		s += dist[(perm[x],perm[x+1])]
	dist_sum.append(s)
print(min(dist_sum))
print(max(dist_sum))