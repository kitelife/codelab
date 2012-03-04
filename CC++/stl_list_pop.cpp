/*
 * stl_list_pop.cpp
 *
 *  Created on: 2011-5-29
 *      Author: xyf
 */
/*
 * list成员函数pop_front()删掉list中的第一个元素，
 * pop_back()删掉最后一个元素。 函数erase()删掉由一
 * 个iterator指出的元素。还有另一个erase()函数可以删掉一个范围的元素。
 */
/*
|| Erasing objects from a list
*/
#include <list>
#include<iostream>

using namespace std;

int main (void) {
  list<int> list1;   // define a list of integers
#
  /*
  || Put some numbers in the list
  || It now contains 0,1,2,3,4,5,6,7,8,9
  */
  for (int i = 0; i < 10; ++i)  list1.push_back(i);
#
  list1.pop_front();    // erase the first element 0
#
  list1.pop_back();     // erase the last element 9
 #
  list1.erase(list1.begin());  // erase the first element (1) using an iterator
#
  list1.erase(list1.begin(), list1.end());  // erase all the remaining elements
#
  cout << "list contains " << list1.size() << " elements" << endl;

  return 0;
}

