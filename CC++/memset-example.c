// Sets the first num bytes of the block of memory pointed by ptr
// to the specified value (interpreted as an unsigned char).
#include <stdio.h>
#include <string.h>

int main()
{
	char str[] = "almost every programmer should know memset!";
	memset(str, '-', 6);
	puts(str);
	return 0;
}