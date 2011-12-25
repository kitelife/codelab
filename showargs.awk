#test sample: awk -v One=1 -v Two=2 -f showargs.awk Three=3 file1 Four=4 file2 file3

BEGIN {
	print "ARGC =", ARGC
	for ( k = 0; k < ARGC; k++)
		print "ARGV[" k "] = [" ARGV[k] "]"
}
