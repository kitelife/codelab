#include <stdio.h>
#include <utmp.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>
/*
#define SHOWHOST
*/
void show_info(struct utmp *utbufp);
void showtime(long timeval);
int main()
{
	struct utmp current_record; //read info into here
	int utmpfd;
	int reclen = sizeof(current_record);

	if( (utmpfd = open(UTMP_FILE, O_RDONLY)) == -1){
		perror( UTMP_FILE );	// UTMP_FILE is in utmp.h
		exit(1);
	}

	while( read(utmpfd, &current_record, reclen) == reclen )
		show_info(&current_record);
	close(utmpfd);
	return 0;
}

void show_info(struct utmp *utbufp)
{
	if(utbufp->ut_type != USER_PROCESS)
		return;
	printf("%-8.8s", utbufp->ut_name);	//the logname
	printf(" ");
	printf("%-8.8s", utbufp->ut_line);	//the tty
	printf(" ");
	showtime(utbufp->ut_time);
	printf(" ");
#ifdef SHOWHOST
	if( utbufp->ut_host[0] != '\0')
		printf("(%s)", utbufp->ut_host);	//the host
#endif
	printf("\n");
}

void showtime( long timeval )
{
	/*
	 *  displays time in a format fit for human consumption
	 *  uses ctime to build a string then picks parts out of it
	 *  Note: %12.12s prints a string 12 chars wide and LIMITS
	 *  it to 12 chars.
	 */
	char *cp;	// to hold address of time
	cp = ctime(&timeval);	// convert time to string
	printf("%12.12s", cp + 4);	// picks 12 chars from pos 4
}
