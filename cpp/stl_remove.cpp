/*
 * stl_remove.cpp
 *
 *  Created on: 2011-5-29
 *      Author: xyf
 */
//通用算法remove()使用和list的成员函数不同的方式工作。一般情况下不改变容器的大小。
/*
|| Using the generic remove algorithm to remove list elements
*/
#include <string>
#include <list>
#include <algorithm>
#include<iostream>

using namespace std;

void PrintIt(string& AString) { cout << AString << endl; }
#
int main (void) {
  list<string> Birds;
  list<string>::iterator NewEnd;
#
  Birds.push_back("cockatoo");
  Birds.push_back("galah");
  Birds.push_back("cockatoo");
  Birds.push_back("rosella");
  Birds.push_back("king parrot");
#
  cout << "Original list" << endl;
  for_each(Birds.begin(), Birds.end(), PrintIt);
#
  NewEnd = remove(Birds.begin(), Birds.end(), "cockatoo");
#
  cout << endl << "List according to new past the end iterator" << endl;
  for_each(Birds.begin(), NewEnd, PrintIt);
#
  cout << endl << "Original list now. Care required!" << endl;
  for_each(Birds.begin(), Birds.end(), PrintIt);
  cout <<endl;
  Birds.erase(NewEnd,Birds.end());
  for_each(Birds.begin(),Birds.end(),PrintIt);
  return 0;
}

