print(sum([len(line.rstrip()) - len(eval(line.rstrip())) for line in open('08.in').readlines()]))
print(sum([line.count('"') + line.count('\\') + 2 for line in open('08.in').readlines()]))