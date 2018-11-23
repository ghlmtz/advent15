import math
from itertools import permutations

weights = []
with open('13.in','r') as f:
	lines = f.readlines()
	L = len(lines)
	ppl = int(math.sqrt(4*L+1)/2 + 0.5)
	for _ in range(ppl):
		weights.append([None] * (ppl))
	n = 0
	i = 0
	for line in lines:
		fields = line.split(' ')
		if i == n:
			n += 1
		if n == ppl:
			break
		weights[i][n] = int(fields[3])
		if fields[2] == "lose":
			weights[i][n] *= -1
		n += 1
		if n == ppl:
			i += 1
			n = 0
	for part2 in range(2):
		if part2:
			for n in range(len(weights)):
				weights[n].append(0)
				weights.append([0] * (ppl+1))
		score = -99999
		for p in permutations([x for x in range(ppl+part2)]):
			our_score = 0
			for m in range(len(p)):
				if m != 0:
					our_score += weights[p[m]][p[m-1]]
				else:
					our_score += weights[p[0]][p[-1]]
				if m != len(p) - 1:
					our_score += weights[p[m]][p[m+1]]
				else:
					our_score += weights[p[-1]][p[0]]
			if our_score > score:
				score = our_score
		print(score)