import urllib
#from BeautifulSoup import *
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
if len(url) < 1:
    url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
    
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
x= []
z=[]
# Retrieve all of the anchor tags
tags = soup('a')
    
for tag in tags:
    #print tag.get('href', None)
    y = tag.get('href', None)
    x.append(y)
print x[2]

url2 = x[2]
html2 = urllib.urlopen(url2).read()
soup = BeautifulSoup(html2)

tags2 = soup('a')
for tag in tags2:
    #print tag.get('href', None)
    w = tag.get('href', None)
    z.append(w)
print z[2]