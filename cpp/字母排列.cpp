/*������ĸͼ���汾1��
��������
����һ������n����������ô�д��ĸ���ɵ��й��ɵ�ͼ�Ρ���n=3����ͼ��
������Щ����n�����޷����������ͼ�εģ���n=30��

����
�����������У�ÿ����һ������n����|n|<60000)��
����ֱ���ļ����������

���
��ÿһ�еĲ������ݣ�����һ���������Case #:�������С�#���ǲ������ݵ��б�ţ���1��ʼ��������ͬһ�������n�ľ���ֵ����ʽ�硰n=3����ð�š�������n֮����һ���ո񡣽����������һ�л���������������ͼ�Ρ�ͼ�ο�������������ĸ���޿ո�β���޶���ո����޷���Ҫ�����������ĸͼ����ô�����No image!����
���һ�����ݺ��һ�С�

�������� 
3
4
�������
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
                  // ������ 
                for(int x=0;x<i;x++)
                 {
                         for(int b=0;b<i-1-x;b++){ cout<<" ";}  //��ӡ�ո� 
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
                       for(int c=0;c<i-1-x;c++) {cout<<" ";}      //��ӡ�ո� 
                        cout<<endl;   
                 }
                 
                 //������ 
                for(int p=i-2;p>=0;p--)
                 {
                         for(int b=0;b<i-1-p;b++){ cout<<" ";}  //��ӡ�ո�
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
                         for(int b=0;b<i-1-p;b++){ cout<<" ";}  //��ӡ�ո�
                        cout<<endl;   
                 }
                cout<<endl;
                a++;
    }
    //system("pause");
    return 0;
}
