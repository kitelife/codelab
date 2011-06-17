'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
for c in range(500,100,-1):
	for a in range(0,333):
		for b in range(100,500):
			if a+b+c==1000 and a*a+b*b==c*c and a<b and b<c:
				print "a=",a,";b=",b,";c=",c
				print a*b*c
