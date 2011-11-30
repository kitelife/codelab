/*秦九韶算法计算多项式的值
问题描述

给定x，计算多项式 的值。要求采用秦九韶算法以尽量减少算术运算的次数。

输入

输入数据文件仅有一行，该行有一个双精度浮点型数据x。

输出

输出计算结果并换行。

输入样例

2.5

输出样例

62.4375

*/
#include<iostream>
using namespace std;
int main()
{
    float i;
    double j;
    cin>>i;
    j=2*i-4;
    j=j*i+1;
    j=j*i+3;
    j=j*i-2;
    j=j*i-6;
    cout<<j<<endl;
    system("pause");
    return 0;
}
