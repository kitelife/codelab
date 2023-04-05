// shows how parent gets child status

#include<stdio.h>
#define DELAY 5

main()
{
	int newpid;
	void child_code(), parent_code();
	printf("%d\n", sizeof(int));
	printf("before: mypid is %d\n", getpid());

	if((newpid=fork()) == -1)
		perror("fork");
	else if(newpid == 0)
		child_code(DELAY);
	else
		parent_code(newpid);
}

// new process takes a nap and then exits

void child_code(int delay)
{
	printf("child %d here. will sleep for %d seconds\n", getpid(), delay);
	sleep(delay);
	printf("child done. about to exit\n");
	exit(17);
}

// parent waits for child then prints a message

void parent_code(int childpid)
{
	int wait_rv;
	int child_status;
	int high_8, low_7, bit_7;
	
	wait_rv= wait(&child_status);

	printf("done waiting for %d. Wait returned: %d\n", childpid, wait_rv);

	high_8 = child_status >> 8;
	low_7 = child_status & 0x7F;
	bit_7 = child_status & 0x80;
	printf("status: exit=%d, sig= %d, core= %d\n", high_8, low_7, bit_7);
}
