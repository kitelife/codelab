#include<stdio.h>
#include<sys/ptrace.h>
#include<sys/wait.h>
#include<unistd.h>

int main()
{
	long long counter = 0;
	int wait_val;	// child's return value
	int pid;	// child's process id

	puts("Please wait:");
	switch(pid = fork()){
		case -1:
			perror("fork");
			break;
		case 0:
			ptrace(PTRACE_TRACEME, 0, 0, 0, 0);
			// must be called in order to allow the control
			// over the child process
			execl("/bin/ls", "ls", NULL);
			// executes the program and causes
			// the child to stop and send a signal
			// to the parent, the parent can now
			// switch to PTRACE_SINGLESTEP
			break;
		default:
			wait(&wait_val);
			// parent waits for child to stop at next instruction
			while(wait_val == 1407){
				counter ++;
				if(ptrace(PTRACE_SINGLESTEP, pid, 0, 0)!=0)
					perror("ptrace");
				// switch to singlestep tracing
				// and release child
				wait(&wait_val);
			}
	}
	printf("Number of machine instructions: %lld\n", counter);
	return 0;
}
