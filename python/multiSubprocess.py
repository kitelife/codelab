import subprocess

def multi(*args):
	for cmd in args:
		p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
		out = p.stdout.read()
		print out
