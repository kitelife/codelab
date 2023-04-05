#include<signal.h>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
//注意只要发出一次SIGINT信号就可以了，因为信号屏蔽只是将信号加入到
//信号阻塞集合中，并没有丢弃这个信号。一旦信号屏蔽取消了，这个信号
//就会发生作用。
int main(int argc, char **argv)
{
	double y;
	sigset_t intmask;
	int i, repeat_factor;
	if(argc!=2)
	{
		fprintf(stderr, "Usage: %s repeat_factor\n\a",argv[0]);
		return 1;
	}
	if((repeat_factor=atoi(argv[1]))<1)
		repeat_factor=10;
	sigemptyset(&intmask); /*将信号集合设置为空*/
	sigaddset(&intmask, SIGINT);/*加入中断Ctrl+C信号*/
	while(1)
	{
		/*阻塞信号，我们不希望保存原来的集合，所以参数为NULL*/
		sigprocmask(SIG_BLOCK,&intmask, NULL);
		fprintf(stderr,"SIGINT signal blocked\n");
		for(i=0;i<repeat_factor;i++)
			y=sin((double)i);
		fprintf(stderr,"Blocked calculation is finished\n");
		/*取消阻塞*/
		sigprocmask(SIG_UNBLOCK,&intmask,NULL);
		fprintf(stderr,"SIGINT signal unblocked\n");
		for(i=0;i<repeat_factor;i++)
			y=sin((double)i);
		fprintf(stderr,"Unblocked calculation is finished\n");
	}
	return 0;
}
