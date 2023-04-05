// purpose: show the skill of looprolling
//
#include<stdio.h>
#include<stdlib.h>

void loop(int n)
{
	int *y=malloc(sizeof(int)*n);
	int i;
	for(i = 0; i < n; i++){
		y[i]=i;
		printf("loop:%d ",y[i]);
	}
	printf("...%d\n",y[i-1]);
	free(y);
}

void loopunroll(int n)
{
	int *y=malloc(sizeof(int)*n);
	int i;
	for(i=0; i < (n % 2); i++){
		y[i] = i;
		printf("loopunroll:%d ",y[i]);
	}
	for(; i+1 < n; i += 2)
	{
		y[i] = i;
		printf("loopunroll:%d ", y[i]);
		y[i+1] = i + 1;
		printf("loopunroll:%d ", y[i+1]);
	}
	printf("...%d\n",y[i-1]);
	free(y);
}

int main()
{
	loop(7);
	loopunroll(7);
	return 0;
}
