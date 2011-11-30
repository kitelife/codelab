/*菱形字母图（版本1）
问题描述
输入一个整数n，输出如下用大写字母构成的有规律的图形。如n=3，有图形
但对有些整数n，是无法输出这样的图形的，如n=30。

输入
输入有若干行，每行有一个整数n，（|n|<60000)。
输入直到文件输入结束。

输出
对每一行的测试数据，先在一行上输出“Case #:”，其中“#”是测试数据的行编号（从1开始），再在同一行上输出n的具体值，格式如“n=3”。冒号“：”与n之间有一个空格。接着在下面的一行或若干行上输出结果图形。图形靠左边输出，两字母间无空格，尾部无多余空格。如无法按要求输出菱形字母图，那么输出“No image!”；
输出一组数据后空一行。

输入样例 
3
4
输出样例
Case 1: n=3
  A
 ABA
ABCBA
 ABA
  A
 
Case 2: n=4
   A
  ABA
 ABCBA
ABCDCBA
 ABCBA
  ABA
   A
*/
#include<iostream>
using namespace std;
int main()
{
    int i,a=1;
    char j;
   while(cin>>i)
    {  
                cout<<"Case "<<a<<": n="<<i<<endl;    
                  // 正三角 
                for(int x=0;x<i;x++)
                 {
                         for(int b=0;b<i-1-x;b++){ cout<<" ";}  //打印空格 
                         for(int y=0;y<=x;y++)
                         {
                                 j='A'+y;
                                 
                                 cout<<j;   
                         }
                         for(int z=x-1;z>=0;z--)
                         {
                                 j='A'+z;
                                 cout<<j;
                                       
                         }
                       for(int c=0;c<i-1-x;c++) {cout<<" ";}      //打印空格 
                        cout<<endl;   
                 }
                 
                 //倒三角 
                for(int p=i-2;p>=0;p--)
                 {
                         for(int b=0;b<i-1-p;b++){ cout<<" ";}  //打印空格
                         for(int q=0;q<=p;q++)
                         {
                                 j='A'+q;
                                 cout<<j;   
                         }
                         for(int r=p-1;r>=0;r--)
                         {
                                 j='A'+r;
                                 cout<<j;
                         }
                         for(int b=0;b<i-1-p;b++){ cout<<" ";}  //打印空格
                        cout<<endl;   
                 }
                cout<<endl;
                a++;
    }
    //system("pause");
    return 0;
}
