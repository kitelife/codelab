/*
 * stl_list_remove.cpp
 *
 *  Created on: 2011-5-29
 *      Author: xyf
 */
//用list成员函数remove()从list中删除元素。
/*
|| Using the list member function remove to remove elements
*/
#include <string>
#include <list>
#include <algorithm>
#include<iostream>
using namespace std;

void PrintIt (const string& StringToPrint) {
  cout << StringToPrint << endl;
}
#
int main (void) {
  list<string> Birds;
#
  Birds.push_back("cockatoo");
  Birds.push_back("galah");
  Birds.push_back("cockatoo");
  Birds.push_back("rosella");
  Birds.push_back("corella");
#
  cout << "Original list with cockatoos" << endl;
  for_each(Birds.begin(), Birds.end(), PrintIt);
 #
  Birds.remove("cockatoo");
#
  cout << "Now no cockatoos" << endl;
  for_each(Birds.begin(), Birds.end(), PrintIt);
  return 0;
}

