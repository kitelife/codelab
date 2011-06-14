#include<sys/time.h>
#include<stdio.h>
#include<unistd.h>
#include<signal.h>
#include<string.h>

#define PROMPT "时间已经过去了两秒钟\n\a"

char *prompt = PROMPT;
unsigned int len;
void prompt_info(int signo)
{
	write(STDERR_FILENO, prompt, len);
}

void init_sigaction(void)
{
	struct sigaction act;
	act.sa_handler = prompt_info;
	act.sa_flags=0;
	sigemptyset(&act.sa_mask);
	sigaction(SIGPROF, &act, NULL);
}

void init_time()
{
	struct itimerval value;
	value.it_value.tv_sec=2;
	value.it_value.tv_usec=0;
	value.it_interval=value.it_value;
	setitimer(ITIMER_PROF,&value,NULL);
}

int main()
{
	len = strlen(prompt);
	init_sigaction();
	init_time();
	while(1);
	return 0;
}
