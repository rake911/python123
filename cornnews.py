import re
name = raw_input("Enter file:")
if len(name) < 1 : name = "newscornmayjune.txt"
handle = open(name)
count = -1
y = range(1755)
dct = {}
names = range(1755)


for line in handle:
	count = int(count) + 1
	names[count] = re.findall('corn', line, re.IGNORECASE)
	if names[count] == ['Corn'] or names[count] == ['corn']:
		dct.update({y[count+1]: line})
				
for key in sorted(dct.iterkeys()):
    print "%s: %s" % (key, dct[key])

import csv

with open('text.csv', 'wb') as csvfile:
    fwriter = csv.writer(csvfile)

    for x in dct:
        fwriter.writerow([x, count])