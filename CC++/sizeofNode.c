#include<stdio.h>

struct node{
	int a;
	char b;
	char c;
	int d;
	char e;
}Node;

int main()
{
	printf("%d\n",sizeof(Node));
	printf("%d\n",sizeof(double));
	return 0;
}
