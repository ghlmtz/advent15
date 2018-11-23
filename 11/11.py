def radd(l, i):
	l[i] += 1
	if l[i] == 26:
		l[i] = 0
		radd(l,i+1)

import string
from itertools import groupby
alpha = string.ascii_lowercase
i = 'vzbxkghb'
numbers = []
for c in i:
	numbers.append(alpha.index(c))
for _ in range(2):
	numbers.reverse()
	while True:
		radd(numbers, 0)
		if 11 in numbers or 14 in numbers or 8 in numbers:
			continue
		for i,N in enumerate(numbers):
			try:
				if numbers[i+1] == N - 1 and numbers[i+2] == numbers[i+1] - 1:
					break
			except IndexError:
				pass
		else:
			continue
		dup = -1
		for i,N in enumerate(numbers):
			try:
				if numbers[i+1] == N and N != dup:
					if dup == -1:
						dup = N
					else:
						break
			except IndexError:
				pass
		else:
			continue
		break
	numbers.reverse()
	print(''.join([alpha[x] for x in numbers]))

