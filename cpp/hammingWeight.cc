#include <iostream>
using namespace std;

int popcount(int x)
{
	int count;
	for(count=0; x; count++)
		x&=x-1;
	return count;
}

int main()
{
	int test1= 0;
	int test2 = 1;
	int test3 = 8;

	cout << popcount(test1) << endl;
	cout << popcount(test2) << endl;
	cout << popcount(test3) << endl;
	cout << popcount(11) << endl;
	return 0;
}
