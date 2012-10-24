/*
	Compares the first num bytes of the block of memory pointed by ptr1 to the first
	num bytes pointed by ptr2, returning zero if they all match or a value different from
	zero representing which is greater if they do not.

	Notice that, unlike strcmp, the function does not stop comparing after finding a null character.
*/

#include <stdio.h>
#include <string.h>

int main()
{
	char buffer1[] = "DWgaOtP12df0";
	char buffer2[] = "DWGAOTP12DF0";

	int n;
	n = memcmp(buffer1, buffer2, sizeof(buffer1));
	if(n>0)
		printf("'%s' is greater than '%s'.\n", buffer1, buffer2);
	else if(n < 0)
		printf("'%s' is less than '%s'.\n", buffer1, buffer2);
	else
		printf("'%s' is the same as '%s'.\n", buffer1, buffer2);

	return 0;
}