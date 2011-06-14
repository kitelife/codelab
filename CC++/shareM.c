/*
 * 父进程将参数写入到共享内存，然后子进程把内容读出来。
 * 最后我们要使用ipcrm释放资源。
 * 先用ipcs找出ID然后用ipcrm shm ID删除.
 * */
#include<stdio.h>
#include<string.h>
#include<errno.h>
#include<unistd.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/shm.h>

#define PERM S_IRUSR|S_IWUSR

int main(int argc, char **argv)
{
	int shmid;
	char *p_addr, *c_addr;
	if(argc!=2)
	{
		fprintf(stderr, "Usage: %s\n\a",argv[0]);
		return 1;
	}
	if((shmid=shmget(IPC_PRIVATE,1024,PERM))==-1)
	{
		fprintf(stderr, "Create Share Memory Error: %s\n\a",strerror(errno));
		return 1;
	}
	if(fork())
	{
		p_addr=shmat(shmid,0,0);
		memset(p_addr,'\0',1024);
		strncpy(p_addr,argv[1],1024);
		return 1;
	}
	else{
		c_addr=shmat(shmid,0,0);
		printf("Client get %s\n",c_addr);
		return 0;
	}
}
