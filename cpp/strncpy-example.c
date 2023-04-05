/*
Copies the first num characters of source to destination. If the end of the source C string
(which is signaled by a null-character) is found before num characters have been copied,
destination is padded with zeros until a total of num characters have been written to it.

No null-character is implicitly appended at the end of destination if source is longer than num
(thus, in this case, destination may not be a null terminated C string).

destination and source shall not overlap(see memmove for a safer alternative when overlapping).

*/

#include <stdio.h>
#include <string.h>

int main()
{
	char str1[] = "To be or not to be";
	char str2[40];
	char str3[40];

	// copy to sized buffer(overflow safe)
	strncpy(str2, str1, sizeof(str2));

	// partial copy (only 5 chars)
	strncpy(str3, str2, 5);
	str3[5] = '\0';	// null character manually added

	puts(str1);
	puts(str2);
	puts(str3);

	return 0;
}