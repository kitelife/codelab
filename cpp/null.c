// Historically, a null pointer has typically corresponded to memory location 0,
// which is usually restricted to the operating system kernel and not accessible to user program.
int a(int *p);

int main(void)
{
	int *p = 0; // null pointer
	return a(p);
}

int a(int *p)
{
	int y = *p;
	return y;
}
