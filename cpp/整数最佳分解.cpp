/*���ŷֽ�����
����������
��n��һ��������������Ҫ��n�ֽ�Ϊ���ɸ�������ͬ����Ȼ���ĺͣ���ʹ��Щ��Ȼ���ĳ˻����
��������Ƕ��ڸ�����������n����̼������ŷֽⷽ����

���룺
�����������У�ÿһ������һ������n����|n|��50����

�����
�������е�ÿ������n���������Ч���룬��ô�����invalid input!��������������ŷֽⷽ�����Դ�С�����˳�����У��м��ÿո�󿪣������ǵĺ���������ĳ˻�m����ʽΪmax=m��

����������
-5
10
1001
���������
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
