/*��������:
       ���Ĵ���˳����뷴�����һ�����ַ��������硰ABCBA������121���ȡ�
       ����������ж���һ�ַ����Ƿ��ǻ��Ĵ���     
����:
      �����ļ��������У�ÿһ����һ��������ݡ�ÿһ�е��ַ���������m���ַ�����m��100�������ǣ�ÿ��ĩβ���Ļ����ַ�������Ϊ��һ�е����ݡ�
���:
      ��ÿһ��������ݣ���һ�����������жϽ�������ǻ��Ĵ����������YES!�������������NO������
��������:
ABCBA
121
ABCA
�������:
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

