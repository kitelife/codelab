/*
 * stl_list_sort.cpp
 *
 *  Created on: 2011-5-29
 *      Author: xyf
 */
#include <string>
#include <list>
#include <algorithm>
#include<iostream>

using namespace std;

void PrintIt (string& StringToPrint) { cout << StringToPrint << endl;}

int main (void) {
  list<string> Staff;
  list<string>::iterator PeopleIterator;

  Staff.push_back("John");
  Staff.push_back("Bill");
  Staff.push_back("Tony");
  Staff.push_back("Fidel");
  Staff.push_back("Nelson");

  cout << "The unsorted list " << endl;
  for_each(Staff.begin(), Staff.end(), PrintIt );

  Staff.sort();

  cout << "The sorted list " << endl;
  for_each(Staff.begin(), Staff.end(), PrintIt);

  return 0;
}

