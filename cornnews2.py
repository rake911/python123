import re
name = raw_input("Enter file:")
if len(name) < 1 : name = "newscornmayjune.txt"
handle = open(name)
count = -1
y = []
x = range(1755)
names = range(1755)


for line in handle:
	count = int(count) + 1
	names[count] = re.findall('corn', line, re.IGNORECASE)
	if names[count] == ['Corn'] or names[count] == ['corn']:
		y.append(line.rstrip())
print len(y)