#include<unistd.h>
#include<stdio.h>
#include<errno.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<dirent.h>
#include<time.h>

static int get_file_size_time(const char *filename)
{
	struct stat statbuf;
	if(stat(filename, &statbuf)==-1)
	{
		printf("Get stat on %s Error: %d\n",filename,strerror(errno));
		return (-1);
	}
	if(S_ISDIR(statbuf.st_mode))
		return (1);
	if(S_ISREG(statbuf.st_mode))
		printf("%s size: %ld bytes \t modified at %s",filename, statbuf.st_size, ctime(&statbuf.st_mtime));
	
	return (0);
}

int main(int argc, char **argv)
{
	DIR *dirp;
	struct dirent *direntp;
	int stats;
	if(argc!=2)
	{
		printf("Usage: %s filename\n\a",argv[0]);
		return (1);
	}
	if(((stats=get_file_size_time(argv[1]))==0)||(stats==-1))
			return (1);
	if((dirp=opendir(argv[1]))==NULL)
	{
		printf("Open Directory %s Error: %d\n",argv[1],strerror(errno));
		return (1);
	}
	while((direntp=readdir(dirp))!=NULL)
		if(get_file_size_time(direntp->d_name)==-1)
			break;
	closedir(dirp);
	return (1);
}
