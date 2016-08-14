#first script is for importing the entire crop progress reports database
#and choosing only the relevant links
import urllib
import re

url = 'http://usda.mannlib.cornell.edu/MannUsda/viewDocumentInfo.do?documentID=1048'
html = urllib.urlopen(url).read()
x = []
htmlreport = []
count = -1
count2 = -1
regextxt = r'https?://[^\s<>"]+|www\.[\S]+'
y = re.findall(regextxt, html)
links = []
regextxt2 = r'.+[t][x][t]'

for i in y:
    z = re.findall(regextxt2, i)
    if z == []: continue
    else:
        x.append(z)


for i in range(len(x)):
    count = count + 1
    w = str(x[count])
    ww = w[2:len(w)-2]
    #print ww
    htmlreport = urllib.urlopen(ww, 'r').read()
    #print htmlreport
    links.append(htmlreport)
#print links[80]
