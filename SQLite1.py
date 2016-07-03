import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
#print fh
import re
count = 0

for line in fh:
    if not line.startswith('From: ') : continue
    count += 1
    pieces = line.split()
    email = pieces[1]
    #print email
    org2 = re.split('.+@', email)
    #print org2[1]
    org = org2[1]
    #print org
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', ( org, ) )
    else :
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
            (org, ))
    # This statement commits outstanding changes to disk each
    # time through the loop - the program can be made faster
    # by moving the commit so it runs only after the loop completes
conn.commit()
x = []
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 100'

print count
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]
    x.append(row[1])

cur.close()
print sum(x)