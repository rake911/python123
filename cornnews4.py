import re
name = raw_input("Enter file:")
if len(name) < 1 : name = "newscornmayjune.txt"
handle = open(name)
count = 0
y = []
z = []
import csv
for line in handle:
	names = re.findall('corn', line, re.IGNORECASE)
	count = count + 1
	if names == ['Corn'] or names == ['corn']:
		y.append(line.rstrip())
		z.append(count)
d = dict(zip(y, z))
d2 = dict((y,x) for x,y in d.iteritems())
with open('sortedcornnews.csv', 'wb') as csvfile:
    fwriter = csv.writer(csvfile)

    for x in sorted(d2.iterkeys()):
        fwriter.writerow([x, d2[x]])