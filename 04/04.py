import hashlib
i = 'yzbqklnj'
n = 1
zeroes = 6	# Change to 5 for part 1
while True:
	data = i + str(n)
	m = hashlib.md5()
	m.update(bytes(data,'utf8'))
	hexstr = m.hexdigest()
	if hexstr[:zeroes] == '0' * zeroes:
		break
	n += 1
print(n)