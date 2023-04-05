#include <iostream>
#include <cstring>
using namespace std;

class String
{
	public:
		String(const char *str = NULL);		//
		String(const String &other);		//
		~String(void);
		String& operator=(const String &other);		//

	private:
		char *m_String;
};

String::~String(void)
{
	cout << "Destructing" << endl;
	if(m_String != NULL)
	{
		delete []m_String;
		m_String = NULL;
	}
}

String::String(const char *str)
{
	cout << "Constructing" << endl;
	if(str == NULL)
	{
		m_String = new char[1];
		*m_String = '\0';
	}
	else
	{
		m_String = new char[strlen(str) + 1];
		strcpy(m_String, str);
	}
}

String::String(const String &other)
{
	cout << "Constructing Copy" << endl;
	m_String = new char[strlen(other.m_String) + 1];
	strcpy(m_String, other.m_String);
}

String& String::operator=(const String &other)
{
	cout << "Operate=Function" << endl;
	if(this == &other)
	{
		return *this;
	}
	delete []m_String;
	m_String = new char[strlen(other.m_String) + 1];
	strcpy(m_String, other.m_String);

	return *this;
}

int main()
{
	String a("hello");
	String b("world");
	String c(a);
	c = b;

	return 0;
}
