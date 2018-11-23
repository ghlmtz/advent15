import re
import json

def recursive_json(j):
	if isinstance(j, dict) and "red" not in j.values():
		return sum([recursive_json(v) for v in j.values()])
	elif isinstance(j, list):
		return sum([recursive_json(x) for x in j])
	elif isinstance(j, int):
		return j
	return 0

print(sum(map(int,re.findall(r'(\-?\d+)',open('12.in','r').read()))))
print(recursive_json(json.loads(open('12.in','r').read())))