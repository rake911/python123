#second script is for importing the database generated in the first, extracting only the relevant
#information and parsing it as a list of lists
import re
from USDASpider import links
print links[90]
regexreport = '^\S+\s\S+[:]'
regexreport2 = '^[0-9]+.+[:]'

cropstages = ['Corn Planted', 'Corn Emerged', 'Corn Silking', 'Corn Dough',
              'Corn Condition', 'Corn Dented', 'Corn Mature', 'Corn Harvested']

linesreport = []

for line in links[90]:
    line = line.rstrip()
    x = re.findall(regexreport, line)
    if len(x) > 0:
        print line
        linesreport.append(line)
    y = re.findall(regexreport2, line)
    if len(y) > 0:
        print line
        linesreport.append(line)
    if line.startswith(cropstages[0]):
        print line
        linesreport.append(line[:12])
    if line.startswith(cropstages[1]):
        print line
        linesreport.append(line[:12])
    if line.startswith(cropstages[2]):
        print line
        linesreport.append(line[:12])
    if line.startswith(cropstages[3]):
        print line
        linesreport.append(line[:10])
    if line.startswith(cropstages[4]):
        print line
        linesreport.append(line[:14])
    if line.startswith(cropstages[5]):
        print line
        linesreport.append(line[:11])
    if line.startswith(cropstages[6]):
        print line
        linesreport.append(line[:11])
    if line.startswith(cropstages[7]):
        print line
        linesreport.append(line[:14])

    if line.startswith('Soybeans'): break
print linesreport
