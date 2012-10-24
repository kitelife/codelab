#include <stdio.h>
#include <assert.h>

static char* strcpy(char *dest, const char *src)
{
	assert(dest != NULL && src != NULL);
	char *ret = dest;
	while((*dest++ = *src++) != '\0');
	return ret;
}

int main()
{
	char str1[] = "Sample string";
	char str2[40];
	char str3[40];
	strcpy(str2, str1);
	strcpy(str3, "copy successful");
	printf("str1: %s\nstr2: %s\nstr3: %s\n", str1, str2, str3);

	return 0;
}