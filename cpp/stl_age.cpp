/*
 * stl_age.cpp
 *
 *  Created on: 2011-5-28
 *      Author: xyf
 */
//关联式容器

#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
	map<string, int, less<string> > name_age;

	name_age["Pohl,Laura"] = 7;
	name_age["Dolsberry,Betty"] = 39;
	name_age["Pohl,Tanya"] = 14;
	cout <<"Laura is "<<name_age["Pohl,Laura"]
	                             << " years old."<<endl;
	return 0;
}

