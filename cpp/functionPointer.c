// 验证函数指针
#include <stdio.h>

int fun(int x)
{
	return x + 5;
}

int main()
{
	int (*f)(int x) = &fun;
	int result = f(5);

	printf("Result: %d\n", result);
	printf("The address of fun: %d\n", fun);
	printf("The address of &fun: %d\n", &fun);
	printf("The address of fun + 1: %d\n", fun + 1);
	printf("The address of &fun + 1: %d\n", &fun + 1);
	return 0;
}
