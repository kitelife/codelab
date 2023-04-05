/*最优分解问题
问题描述：
设n是一个正整数。现在要求将n分解为若干个互不相同的自然数的和，且使这些自然数的乘积最大。
你的任务是对于给定的正整数n，编程计算最优分解方案。

输入：
输入有若干行，每一行上是一个整数n，（|n|￡50）。

输出：
对输入中的每个整数n，如果是无效输入，那么输出“invalid input!”，否则输出最优分解方案，以从小到大的顺序排列，中间用空格阁开，在它们的后面输出最大的乘积m，格式为max=m。

输入样例：
-5
10
1001
输出样例：
invalid input!
2 3 5 max=30
invalid input!
*/

#include<iostream>
using namespace std;
int main()
{
    int x,y,z,p;
    int a,b,c;
    a=1;
    b=1;
    c=1;
    y=0;
    z=2;
    cin>>x;
    if(x<1||x>50)
    cout<<"invalid input!"<<endl;
    else 
    {
         while(y<x)
         {
           y+=z++;
         }  
         z=z-1;
         p=y-x;
         if(p==0)
         {
              for(int j=2;j<=z;j++)
              {
                  cout<<j<<" ";
                  a*=j;
              }
              cout<<"max="<<a<<endl;
           
         }   
         else if(p==1)
         {
              for(int j=3;j<z;j++)
              {
                  cout<<j<<" ";
                  b*=j;
              }
              cout<<z+1<<" ";
              cout<<"max="<<b*(z+1)<<endl;
         }
         else
         {
             for(int j=2;j<=z;j++)
             {
                  if(j!=p)
                  {
                          cout<<j<<" ";
                          c*=j;
                  }
             }
         cout<<"max="<<c<<endl;
        } 
    }     
    system("pause");
    return 0;
}
