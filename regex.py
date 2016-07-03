name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_254424.txt"
handle = open(name)
count = 0
y = []
x = []
z = []
import re

for line in handle:
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        count = count + 1
        for i in range(len(x)):
            x[i] = int(x[i])
        y.append(x)

for i in range(len(y)):
    z.append(sum(y[i]))
print sum(z)