# From the book 《Automating System Administration with Perl》
opendir my $DIR, '.' or die "Can't open the current directory: $!\n";
# read file/directory names in that directory into @names
my @names = readdir $DIR or die "Unable to read current dir:$!\n";
closedir $DIR;
foreach my $name (@names) {
   next if ($name eq '.');   # skip the current directory entry
   next if ($name eq '..');  # skip the parent directory entry
   if (-d $name) {           # is this a directory?
      print "found a directory: $name\n";
      next;                  # can skip to the next name in the for loop
   }
   if ($name eq 'core') {    # is this a file named "core"?
     print "found one!\n";
  }
}