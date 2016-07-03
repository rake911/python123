name = input("Enter file:")
if len(name) == 0:
	name = "mbox-short.txt"
fh = open(name)
import re
x = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x.append(float(line[20 : 100]))
print(x)
print(sum(x)/len(x))

