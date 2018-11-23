import re
i = '1113122113'
for N in range(50):
	newstr = ''
	for m in re.finditer(r'(\d)\1*',i):
		s = m.group()
		newstr += '%d'%len(s) + s[0]
	i = newstr
	if N == 39:
		print(len(i))
print(len(i))
