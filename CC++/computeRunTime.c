#include<sys/time.h>
#include<stdio.h>
#include<math.h>

void function(){
	unsigned int i, j;
	double y;
	for(i=0;j<1000;i++)
		for(j=0;j<1000;j++)
			y=sin((double)i);
}

int main(int argc, char **argv)
{
	struct timeval tpstart, tpend;
	float timeuse;
	gettimeofday(&tpstart,NULL);
	function();
	gettimeofday(&tpend,NULL);
	timeuse=1000000*(tpend.tv_sec-tpstart.tv_sec)+tpend.tv_usec-tpstart.tv_usec;
	timeuse /=1000000;
	printf("tpend-tpstart: %f, %f\n",(double)(tpend.tv_sec-tpstart.tv_sec),(double)(tpend.tv_usec-tpstart.tv_usec));
	printf("Used Time: %f\n",timeuse);
	return (0);
}
