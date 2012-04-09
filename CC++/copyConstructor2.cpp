#include <iostream>
#include <cstring>

using namespace std;

class Test
{
	public:
		char *buf;
		
		Test(void)
		{
			buf = NULL;
		}
		
		Test(const char* str)
		{
			buf = new char[strlen(str) + 1];
			strcpy(buf, str);
		}

		Test(Test &test)
		{
			buf = new char[strlen(test.buf) + 1];
			strcpy(buf, test.buf);
		}

		~Test()
		{
			if(buf != NULL)
			{
				delete buf;		//释放buf指向的堆内存
				buf = NULL;
			}
		}
};

int main()
{
	Test t1("hello");
	Test t2 = t1;			// 调用默认的复制构造函数

	cout << "(t1.buf == t2.buf)?" <<
		(t1.buf == t2.buf ? "yes":"no") << endl;

	return 0;
}
