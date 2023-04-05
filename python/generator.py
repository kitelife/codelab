def pyrevgen(seq):
    for i, elem in enumerate(reversed(seq)):
        yield i, elem

for i, e in pyrevgen(['a', 'b', 'c']):
    print (i, e)
