import sys

count = {}
for filename in sys.argv[1:]:
    infile = open(filename, 'r')
    for line in infile:
        name = line.strip()
        count[name] = count.get(name, 0) + 1
    infile.close()
#print
keys = count.keys()
keys.sort()
for b in keys:
    print b, count[b]