import re
# Part one
lights = {}
for line in open('06.in','r').readlines():
	m = re.search('(.*) (\d+),(\d+) through (\d+),(\d+)',line)
	if m:
		x1,y1,x2,y2 = tuple(map(int,m.group(2,3,4,5)))
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				if m.group(1) == 'turn on':
					lights[(x,y)] = 1
				elif m.group(1) == 'turn off':
					lights[(x,y)] = 0
				else:
					lights[(x,y)] = (lights.get((x,y),0)+1)%2
print(sum(lights.values()))
# Part two
lights = {}
for line in open('06.in','r').readlines():
	m = re.search('(.*) (\d+),(\d+) through (\d+),(\d+)',line)
	if m:
		x1,y1,x2,y2 = tuple(map(int,m.group(2,3,4,5)))
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				if m.group(1) == 'turn on':
					lights[(x,y)] = lights.get((x,y),0)+1
				elif m.group(1) == 'turn off':
					lights[(x,y)] = max(0,lights.get((x,y),0)-1)
				else:
					lights[(x,y)] = lights.get((x,y),0)+2
print(sum(lights.values()))					