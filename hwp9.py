name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = 0
x = []
dct = {}
names =[]

for line in handle:
    if not line.startswith("From ") : continue
    count = int(count) + 1
    x = line.split()
    names.append(x[1])

for name in names:  
  if name not in dct:  
    dct[name]= 1  
  else:  
    dct[name] = dct[name] + 1  
print (dct)

#alternative:

for name in names:
	dct[name] = dct.get(name,0) + 1
print (dct)

bign = None
bigc = None

for name,count in dct.items():
    if bigc is None or count > bigc:
        bigc = count
        bign = name
        
print(bign, bigc)