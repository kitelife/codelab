/*
 * stl_vect.cpp
 *
 *  Created on: 2011-5-28
 *      Author: xyf
 */
#include<iostream>
#include<deque>
#include<vector>

using namespace std;

int main()
{
	int data[5] = {6, 8, 7, 6, 5};
	vector<int> v(5, 6);   //5个元素的向量，全部初始化为6
	deque<int> d(data, data+5);
	deque<int>::iterator p;
	cout << "\nDeque values"<<endl;
	for(p = d.begin(); p!= d.end(); ++p)
		cout << *p << '\t';
	cout << endl;
	d.insert(d.begin(), v.begin(), v.end());
	for(p = d.begin(); p!= d.end(); p++)
		cout << *p <<'\t';

	return 0;
}

