import urllib
import re
url = 'http://usda.mannlib.cornell.edu/MannUsda/viewDocumentInfo.do?documentID=1048'
html = urllib.urlopen(url).read()
x = []

regextxt = r'https?://[^\s<>"]+|www\.[\S]+[t][x][t]'
y = re.findall(regextxt, html)

regextxt2 = r'.+[t][x][t]'

for i in y:
    z = re.findall(regextxt2, i)
    if z == []: continue
    else:
        x.append(z)

w = str(x[0])
w = w[2:len(w)-2]

htmlreport = urllib.urlopen(w)
regexreport = '^\S+\s\S+[:]'
regexreport2 = '^[0-9]+.+[:]'

cropstages = ['Corn Planted', 'Corn Emerged', 'Corn Silking', 'Corn Dough', 'Corn Condition', 'Corn Dented', 'Corn Mature', 'Corn Harvested']
linesreport = []

for line in htmlreport:
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

    if line.startswith('Soybeans Blooming'): break
print linesreport
