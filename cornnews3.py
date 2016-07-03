import re
name = raw_input("Enter file:")
if len(name) < 1 : name = "newscornmayjune.txt"
handle = open(name)
count = 0
y = []
names = []


for line in handle:
	names = re.findall('corn', line, re.IGNORECASE)
	count = count + 1
	if names == ['Corn'] or names == ['corn']:
		y.append(line.rstrip())
		print line,count
#print len(y)
#print y
