import urllib
#from BeautifulSoup import *
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
if len(url) < 1:
    url = 'http://python-data.dr-chuck.net/known_by_Aray.html'
    
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
x= []
z=[]
tags = soup('a')
    
for tag in tags:
    y = tag.get('href', None)
    x.append(y)
print x[17]