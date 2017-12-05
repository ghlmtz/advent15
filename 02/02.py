s = 0
a = 0
for line in open('02.in','r').readlines():
	l,w,h = [int(x) for x in sorted(line.rstrip().split('x'),key=int)]
	s += 3*l*w + 2*w*h + 2*h*l
	a += 2*(l+w) + l*w*h
print(s) # Part one
print(a) # Part two