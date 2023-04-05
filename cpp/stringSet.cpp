#include <string>
#include <set>
#include <iostream>

using namespace std;

int main()
{
	set<string> S;
	set<string>::iterator j;
	string t;
	while(cin >> t)
		S.insert(t);
	for(j = S.begin(); j != S.end(); ++j)
		cout << *j << "\n";

	return 0;
}
