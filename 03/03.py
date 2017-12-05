i = open('03.in','r').read().rstrip()
houses = {}
pos = (0,0)
pos2 = (0,0)
dirs = {'>': (0,1), '<': (0,-1), '^': (-1,0), 'v': (1,0)}
houses[pos] = houses.get(pos,0) + 1
for N in range(0,len(i),2):
	pos = tuple(map(sum,zip(pos,dirs[i[N]])))
	houses[pos] = houses.get(pos,0) + 1
	# Uncomment for step one code
	# pos = tuple(map(sum,zip(pos,dirs[i[N+1]])))
	# houses[pos] = houses.get(pos,0) + 1
	# Comment for step one code
	pos2 = tuple(map(sum,zip(pos2,dirs[i[N+1]])))
	houses[pos2] = houses.get(pos2,0) + 1
print(len(houses))