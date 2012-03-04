#include<stdio.h>
#include<string.h>

int main()
{
	char str[] = "now # is the time for all # good men to come to the # aid of their country";
	char delims[] = "#";
	char *result = NULL;

	result = strtok(str, delims);

	while(result != NULL){
		printf("result is \"%s\"\n", result);
		result = strtok(NULL, delims);
	}

	return 0;
}
