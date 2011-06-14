#include<unistd.h>
#include<stdio.h>
#include<errno.h>
#include<fcntl.h>
#include<string.h>
#include<sys/types.h>
#include<sys/stat.h>

#define BUFFER_SIZE 1024
int main(int argc, char **argv)
{
	int fd;
	char buffer[BUFFER_SIZE];
	if(argc!=2)
	{
		fprintf(stderr,"Usage: %s outfilename\n\a",argv[0]);
		return (1);
	}
	if((fd=open(argv[1],O_WRONLY|O_CREAT|O_TRUNC,S_IRUSR|S_IWUSR))==-1)
	{
		fprintf(stderr,"Open %s Error: %s\n\a",argv[1],strerror(errno));
		return (1);
	}
	if(dup2(fd,STDOUT_FILENO)==-1)
	{
		fprintf(stderr,"Redirect Standard Out Error: %s\n\a",strerror(errno));
		return (1);
	}
	fprintf(stderr,"Now, please input string");
	fprintf(stderr,"(To quit use CTRL+D)\n");
	while(1)
	{
		fgets(buffer,BUFFER_SIZE,stdin);
		if(feof(stdin))
			break;
		write(STDOUT_FILENO,buffer,strlen(buffer));
	}
	return (0);
}
