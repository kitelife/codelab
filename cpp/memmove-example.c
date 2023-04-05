/*
* Copies the values of num bytes from the location pointed by
* source to the memory block pointed by destination.
* Copying takes place as if an intermediate buffer were used,
* allowing the destination and source to overlap.
*/

#include <stdio.h>
#include <string.h>

int main()
{
	char str[] = "memmove can be very useful......";
	memmove(str+20, str+15, 11);
	puts(str);
	return 0;
}