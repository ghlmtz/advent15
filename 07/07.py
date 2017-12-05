signals = [x.split() for x in open('07.in','r').readlines()]
wires = len([x[-1] for x in signals])
values = {}
def parse(x):
	if x[0].isdigit():
		return int(x)
	elif x in values:
		return values[x]
	else:
		return None
while 'a' not in values:
	next_sig = []
	for sig in signals:
		if sig[0][0].isdigit() and sig[1] == '->':
			values[sig[2]] = int(sig[0])
		elif sig[0] == 'NOT' and sig[1] in values:
			values[sig[3]] = (~values[sig[1]])%65536
		else:
			a = parse(sig[0])
			if a != None:
				if sig[1] == 'LSHIFT':
					values[sig[4]] = (a << int(sig[2]))%65536
				elif sig[1] == 'RSHIFT':
					values[sig[4]] = (a >> int(sig[2]))%65536
				elif sig[1] == '->':
					values[sig[2]] = a
				else:
					b = parse(sig[2])
					if b != None:
						if sig[1] == 'AND':
							values[sig[4]] = a & b
						elif sig[1] == 'OR':
							values[sig[4]] = a | b

					else:
						next_sig.append(sig)
			else:
				next_sig.append(sig)
		values['b'] = 3176	# Comment out for part 1
	signals = next_sig
print(values['a'])