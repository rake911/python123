import urllib
#from BeautifulSoup import *
from bs4 import BeautifulSoup
x= []
url = raw_input('Enter - ')
if len(url) < 1:
    url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
    
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
for tag in tags:
    #print tag.get('href', None)
    y = tag.get('href', None)
    x.append(y)
#print x[2]

for i in range(0, 3):
    #url[i] = x[2]
    html[i] = urllib.urlopen(url[i]).read()
    soup[i] = BeautifulSoup(html[i])
    tags[i] = soup[i]('a')
    for tag in tags:
        #print tag.get('href', None)
        y = tag.get('href', None)
        x.append(y)
    print x[2]

