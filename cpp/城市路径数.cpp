/*����1����x����ת�������2�ĵ���������*/
#include<iostream>
using namespace std;

int main()
{
    int i,j,k,n,m,temp;
    cin>>n;         //ȷ�����е���Ŀ 
    int array[n][n];  
    int outarray[n][n];       
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            cin>>m;
            if(i==j&&m!=0)
            {
                cout<<"the number("<<i<<", "<<j<<")is error! please input again"<<endl;
                cin>>m;
            }
            array[i][j]=m;      //n����������֮���ֱ��ͨ·����Ŀ 
        }
    }
   
    cout<<array[0][0]<<endl;;           //���� 
    
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            outarray[i][j]=0;      
        }
    }
    cout<<outarray[n-1][n-1]<<endl;       //���� 
    
    cout<<"-----------"<<endl;

    for(i=0;i<n;i++)
    { 
		for(j=0;j<n;j++)
		{
			for(k=0;k<n;k++)
			{
				temp=(array[i][k])*(array[k][j]);
                outarray[i][j]=outarray[i][j]+temp;
                                    }
            }
    }
    
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
			cout<<outarray[i][j]<<" ";
        }
        cout<<endl;
    }
    
    return 0;
}
 
