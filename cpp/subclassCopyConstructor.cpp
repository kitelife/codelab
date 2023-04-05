#include <iostream>
using namespace std;

class Base
{
	public:
		Base():i(0){cout << "Base()" << endl;}

		Base(int n):i(n){cout << "Base(int)" << endl;}

		Base(const Base &b):i(b.i)		//复制构造函数
		{
			cout << "Base(Base&)" << endl;
		}
	private:
		int i;
};

class Derived : public Base
{
	public:
		Derived():Base(0), j(0){cout << "Derived()" << endl;}
		
		Derived(int m, int n):Base(m), j(n) {cout << "Derived(int)" << endl;}
		
		// Derived类的复制构造函数，调用了Base的复制构造函数
		Derived(const Derived &obj):Base(obj),j(obj.j)
		{
			cout << "Derived(Derived&)" << endl;
		}
	private:
		int j;
};

int main()
{
	Base b(1);
	Derived obj(2, 3);
	cout << "--------------" << endl;
	Derived d(obj);
	cout << "--------------" << endl;

	return 0;
}
