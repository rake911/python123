fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print line
    count = float(count) + 1
    #print count
    x = float(line[20 : 100])
y = x/count
print "Average spam confidence: ", y
