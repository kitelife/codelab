#include <map>
#include <string>
#include <iostream>

using namespace std;

int main(void)
{
	map<string, int> M;
	map<string, int>::iterator j;
	string t;
	while(cin >> t)
		M[t] ++;
	for(j = M.begin(); j != M.end(); ++j)
		cout << j->first << " " << j->second << endl;

	return 0;
}
