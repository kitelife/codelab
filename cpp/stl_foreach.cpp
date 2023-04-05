/*
 * stl_foreach.cpp
 *
 *  Created on: 2011-5-29
 *      Author: xyf
 */
#include<iostream>
#include<string>
#include<list>
#include<algorithm>

using namespace std;

void PrintIt(string& StringToPrint){
	cout << StringToPrint <<endl;
}

int main(){
	list<string>FruitAndVegetables;
	FruitAndVegetables.push_back("carrot");
	FruitAndVegetables.push_back("pumpkin");
	FruitAndVegetables.push_back("potato");
	FruitAndVegetables.push_front("apple");
	FruitAndVegetables.push_front("pineapple");

	for_each(FruitAndVegetables.begin(),FruitAndVegetables.end(),PrintIt);
	return 0;
}



