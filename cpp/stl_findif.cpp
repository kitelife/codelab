/*
 * stl_findif.cpp
 *
 *  Created on: 2011-5-29
 *      Author: xyf
 */
#include <string>
#include <list>
#include <algorithm>
#include<iostream>

using namespace std;

class EventIsIn1997 {
public:
 bool operator () (string& EventRecord) {
   // year field is at position 12 for 4 characters in EventRecord
   return EventRecord.substr(12,4)=="1997";
  }
};

int main () {
  list<string> Events;

// string positions 0123456789012345678901234567890123456789012345
  Events.push_back("07 January  1995  Draft plan of house prepared");
  Events.push_back("07 February 1996  Detailed plan of house prepared");
  Events.push_back("10 January  1997  Client agrees to job");
  Events.push_back("15 January  1997  Builder starts work on bedroom");
  Events.push_back("30 April    1997  Builder finishes work");

  list<string>::iterator EventIterator =
      find_if (Events.begin(), Events.end(), EventIsIn1997());

  // find_if completes the first time EventIsIn1997()() returns true
  // for any object. It returns an iterator to that object which we
  // can dereference to get the object, or if EventIsIn1997()() never
  // returned true, find_if returns end()
  if (EventIterator==Events.end()) {
    cout << "Event not found in list" << endl;
  }
  else {
   cout << *EventIterator << endl;
  }
  return 0;
}

