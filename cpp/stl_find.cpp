/*
 * stl_find.cpp
 *
 *  Created on: 2011-5-29
 *      Author: xyf
 */
#include <string>
#include <list>
#include <algorithm>
#include<iostream>

using namespace std;

int main () {
  list<string> Fruit;
  list<string>::iterator FruitIterator;

  Fruit.push_back("Apple");
  Fruit.push_back("Star Apple");
  Fruit.push_back("Pineapple");

  FruitIterator = find (Fruit.begin(), Fruit.end(), "Pineapple");

  if (FruitIterator == Fruit.end()) {
    cout << "Fruit not found in list" << endl;
  }
  else {
   cout << *FruitIterator << endl;
  }
  //cout <<*Fruit.begin()<<"     "<< *Fruit.end()<<endl;
  return 0;
}
