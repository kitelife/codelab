#include <stdio.h>

long filesize(FILE *stream);

int main(void)
{
	FILE *stream;

	stream = fopen("MyFile.txt", "w+");
	fprintf(stream, "This is a test");
	printf("FileSize of MyFile.txt is %ld bytes\n", filesize(stream));
	fclose(stream);

	return 0;
}

long filesize(FILE *stream)
{
	long curpos, length;

	curpos = ftell(stream);
	fseek(stream, 0L, SEEK_END);
	length = ftell(stream);
	fseek(stream, curpos, SEEK_SET);

	return length;
}
