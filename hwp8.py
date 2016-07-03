fname = input("Enter file name: ")
if len(fname) == 0:
	fname = "romeo.txt"
fh = open(fname)
lst = range(5)
count = 0
x = range(40)
for line in fh:
    count = int(count) + 1
    line = line.rstrip()
    lst[count] = line.split()
lst = lst[1:5]
for line in lst:
    count = int(count) + 1
    for word in line:
        if word in line: 
        	x[count] = x.append(word)
y = x[40:]
z = sorted(y)
w = range(len(z))
count = -1
for word in z:
    count = int(count) + 1
    if word not in w:
        w[count] = w.append(word)
ans = w[33:]
print ans

#figured out a shorter version
fname = raw_input("Enter file name: ")
if len(fname) == 0:
	fname = "romeo.txt"
fh = open(fname)
lst = list()
w = range(30)
count = -1

for line in fh:
    lst = line.split()
    count = int(count) + 1
    for word in lst:
    	if word not in w:
             w[count] = w.append(word)

z = sorted(w[30:])           
print z 

#and another tweak
fname = raw_input("Enter file name: ")
if len(fname) == 0:
	fname = "romeo.txt"
fh = open(fname)
lst = list()
w = range(5)
count = 0
y = len(w)

for line in fh:
    lst = line.split()
    count = int(count) + 1
    for word in lst:
        if word not in w:
             w[count] = w.append(word)
        
z = sorted(w[y:])           
print z 

#next assignment
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
x = range(30)

for line in fh:
    if not line.startswith("From ") : continue
    count = int(count) + 1
    x = line.split()
    print x[1]
	
print "There were", count, "lines in the file with From as the first word"