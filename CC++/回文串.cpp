/*问题描述:
       回文串是顺序读与反序读都一样的字符串，例如“ABCBA”、“121”等。
       你的任务是判断任一字符串是否是回文串。     
输入:
      输入文件有若干行，每一行是一组测试数据。每一行的字符串至多有m个字符，（m≤100），但是，每行末尾处的换行字符不能作为这一行的内容。
输出:
      对每一组测试数据，在一行上输出你的判断结果。若是回文串，则输出“YES!”，否则输出“NO！”。
输入样例:
ABCBA
121
ABCA
输出样例:
YES!
YES!
NO!*/
#include<iostream>
using namespace std;
int main()
{
    int length,x,y,sum;
    char s[100];
    cin>>s;
    length=strlen(s);
    cout<<s<<endl;
    cout<<length<<endl;
    sum=0,x=0;
    y=length/2;
    cout<<"is it a huiwenchuan?"<<endl;
    for(int i=0;i<=y;i++)
    {
            if(s[i]==s[length-i-1])
            x=0;
            else x=1;
            sum+=x;
    }
    if(sum==0)
    cout<<"yes!"<<endl;
    else cout<<"no!"<<endl;
    system("pause");
    return 0;
}

