#include<stdio.h>
#include<unistd.h>
#include<limits.h>
#include<errno.h>
#include<string.h>
#include<stdlib.h>
#include<sys/stat.h>
#include<sys/wait.h>
#include<sys/ipc.h>
#include<sys/sem.h>

#define PERMS S_IRUSR|S_IWUSR

void init_semaphore_struct(struct sembuf *sem,int semnum,int semop,int semflg)
{
	/*初始化信号灯结构*/
	sem->sem_num=semnum;
	sem->sem_op=semop;
	sem->sem_flg=semflg;
}

int del_semaphore(int semid)
{
	/*
	 * 信号灯并不随程序的结束而被删除，如果我们没删除的话（将1改成0）
	 * 可以用ipcs命令查看到信号灯，用ipcrm可以删除信号灯
	 * */
#if 1
	return semctl(semid,0,IPC_RMID);
#endif
}

int main(int argc, char **argv)
{
	char buffer[MAX_CANON], *c;
	int i, n;
	int semid, semop_ret, status;
	pid_t childpid;
	struct sembuf semwait, semsignal;
	if((argc!=2)||((n=atoi(argv[1]))<1))
	{
		fprintf(stderr, "Usage: %s number\n\a",argv[0]);
		return 1;
	}
	/*
	 * 使用IPC_PRIVATE表示由系统选择一个关键字来创建
	 * 创建以后信号灯的初始值为0
	 * */
	if((semid=semget(IPC_PRIVATE,1,PERMS))==-1)
	{
		fprintf(stderr, "[%d]: Acess Semaphore Error: %s\n\a",getpid(),strerror(errno));
		return 1;
	}
	/*semwait是要求资源的操作(-1)*/
	init_semaphore_struct(&semwait,0,-1,0);
	/*semsignal是释放资源的操作(+1)*/
	init_semaphore_struct(&semsignal,0,1,0);
	/*开始的时候有一个系统资源(一个标准错误输出)*/
	if(semop(semid,&semsignal,1)==-1)
	{
		fprintf(stderr,"[%d]: Increment Semaphore Error: %s\n\a",getpid(),strerror(errno));
		if(del_semaphore(semid)==-1)
			fprintf(stderr,"[%d]:Destroy Semaphore Error: %s\n\a",getpid(),strerror(errno));
		return 1;
	}
	/*创建一个进程链*/
	for(i=0;i<n;i++)
		if((childpid=fork()))
			break;
	sprintf(buffer,"[i=%d]-->[Process=%d]-->[Parent=%d]-->[Child=%d]\n",i,getpid(),getppid(),childpid);
	c=buffer;
	/*这里要求资源，进入原子操作*/
	while(((semop_ret=semop(semid,&semwait,1))==-1)&&(errno==EINTR));
	if(semop_ret==-1)
	{
		fprintf(stderr,"[%d]: Decrement Semaphore Error: %s\n\a",getpid(),strerror(errno));
	}
	else{
		while(*c!='\0')
			fputc(*c++,stderr);
		/*原子操作完成，赶快释放资源*/
		while(((semop_ret=semop(semid,&semsignal,1))==-1)&&errno==EINTR);
		if(semop_ret==-1)
			fprintf(stderr,"[%d]: Increment Semaphore Error: %s\n\a",getpid(),strerror(errno));
	}
	/*不能够在其他进程访问信号灯的时候，我们删除了信号灯*/
	while((wait(&status)==-1)&&(errno==EINTR));
	/*信号灯只能够被删除一次*/
	if(i==1)
		if(del_semaphore(semid)==-1)
			fprintf(stderr,"[%d] Destroy Semaphore Error: %s\n\a",getpid(),strerror(errno));
	return 0;
}
