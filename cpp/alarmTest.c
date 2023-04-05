#include<unistd.h>
#include<stdio.h>
//alarm函数可以在seconds秒之后向自己发送一个SIGALRM信号。
//SIGALRM的缺省操作是结束进程，所以程序在1秒之后结束。
//你可以看看你的最后I值为多少，比较一下大家的系统性能差异
int main()
{
	unsigned int i;
	alarm(1);
	for(i=0;1;i++)
		printf("I= %d\n",i);
}
