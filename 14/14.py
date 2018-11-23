with open('14.in','r') as file:
	data = []
	lines = file.readlines()
	for N,line in enumerate(lines):
		data.append([])
		fields = line.split(' ')
		for f in fields:
			if f.isdigit():
				data[N].append(int(f))
dist = [0] * len(data)
state = [1] * len(data)
timer = [data[x][1] for x in range(len(data))]
scores = [0] * len(data)
for _ in range(2503):
	for i in range(len(data)):
		if state[i]:
			dist[i] += data[i][0]
		timer[i] -= 1
		if timer[i] <= 0:
			if state[i]:
				state[i] = 0
				timer[i] = data[i][2]
			else:
				state[i] = 1
				timer[i] = data[i][1]
	for i in range(len(data)):
		if dist[i] == max(dist):
			scores[i] += 1
print(max(dist))
print(max(scores))
