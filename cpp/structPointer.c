// 验证结构体指针
//
#include <stdio.h>

struct sample{
	int t;
	char v;
};

int main()
{
	struct sample *sa =(struct sample *)malloc(sizeof(struct sample));
	struct sample sb = *sa;
	sa->t = 2;
	sa->v = 'a';

	printf("The address sa: %d\n", sa);
	printf("The address sb: %d\n", &sb);
	printf("%d\n", sa[0]);
	
	int array[5] = {0,1,2,3,4};
	printf("%d\n",*array);
	printf("%d\n",array);
	printf("%d\n",array[0]);
	
	return 0;
}
