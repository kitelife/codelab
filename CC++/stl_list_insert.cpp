/*
 * stl_list_insert.cpp
 *
 *  Created on: 2011-5-29
 *      Author: xyf
 */
/*
|| Using insert to insert elements into a list.
*/
#include <list>
#include<iostream>
#include<algorithm>

using namespace std;

void PrintIt(int& item){
	cout << item <<endl;
}

int main (void) {
  list<int> list1;
#
  /*
  || Put integers 0 to 9 in the list
  */
  for (int i = 0; i < 10; ++i)  list1.push_back(i);
#
  /*
  || Insert -1 using the insert member function
  || Our list will contain -1,0,1,2,3,4,5,6,7,8,9
  */
  list1.insert(list1.begin(), -1);
#
  /*
  || Insert an element at the end using insert
  || Our list will contain -1,0,1,2,3,4,5,6,7,8,9,10
  */
  list1.insert(list1.end(), 10);
 #
  /*
  || Inserting a range from another container
  || Our list will contain -1,0,1,2,3,4,5,6,7,8,9,10,11,12
  */
  int IntArray[2] = {11,12};
  list1.insert(list1.end(), &IntArray[0], &IntArray[2]);
#
  /*
  || As an exercise put the code in here to print the lists!
  || Hint: use PrintIt and accept an interger
  */
  for_each(list1.begin(),list1.end(),PrintIt);
  return 0;
}
