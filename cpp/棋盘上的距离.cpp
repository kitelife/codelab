#include<iostream>
using namespace std;

/*��*/
int wang(int i,int j,int x,int y)
{
    int a,b;
    a=abs(x-i);
    b=abs(y-j);
    if(a>=b)
    return a;
    else
    return b;
}
/*��*/
int hou(int i,int j,int x,int y)
{   
    int a,b;
    a=abs(x-i);
    b=abs(y-j);
    if(a==0&&b==0)
    return 0;
    else if(a==b)
    return 1;
    else if(a!=0&&b!=0)
    return 2;
    
}
/*��*/
int ju(int i,int j,int x,int y)
{
    int a,b;
    a=x-i;
    b=y-j;
    if(a==0&&b==0)
    return 0;
    if(a!=0&&b!=0)
    return 2;
    else return 1;
} 
/*��*/
int xiang(int i,int j,int x,int y)
{
    int a,b;
    a=abs(x-i);
    b=abs(y-j);
    
    if(a==0&&b==0)
    return 0;
    
    else if(abs(a-b)%2!=0)
    return -1;
    
    else if(a==b)
    return 1;
    
    else if(abs(a-b)%2==0)
    return 2;
} 
int main()
{
    int i,j,x,y;
    while(cin>>i>>j>>x>>y)
    {
                          if(i>0&&i<9&&0<j&&j<9&&0<x&&x<9&&0<y&&y<9)
                          {
                          cout<<"��: "<<wang(i,j,x,y)<<endl;  
                          cout<<"��: "<<hou(i,j,x,y)<<endl;
                          cout<<"��: "<<ju(i,j,x,y)<<endl;
                          cout<<"��: "<<xiang(i,j,x,y)<<endl;
                          }
                          else 
                          cout<<"the number is invalid!!!" <<endl;
    }
    system("pause");
    return 0;
}
