#include <iostream>
using namespace std;

class Test
{
	public:
		int a;

		Test(int x)
		{
			a = x;
		}
		
		Test(const Test &test)	//copy constructor
		{
			cout << "copy constructor" << endl;
			a = test.a;
		}

};

void fun1(Test test)
{
	cout << "fun1()..." << endl;
}

Test fun2()
{
	Test t(2);
	cout << "func2()..." << endl;
	return t;
}

int main()
{
	Test t1(1);
	cout << "----------" << endl;
	Test t2 = t1;
	cout << "before fun1()..." << endl;
	fun1(t1);

	Test t3 = fun2();
	cout << t3.a << endl;
	cout << "after fun2()..." << endl;
	return 0;
}
