/*�ƶ��ڴ��㷨
������K��Ԫ�ص�����int a[K]={...}��дһ����Ч�㷨����������ѭ������mλ��
���磺int a[6]={1,2,3,4,5,6},ѭ������3λ�õ��Ľ��{456123}
Ҫ��
1.������������������ռ䣬�������������������
2.���������ÿ������*/
#include<stdio.h>
#include<stdlib.h>
#define Len 8

/*�����Լ���ĺ���*/
int CommonFactor(int m,int n)
{
    int tmp;
    if(m<n)
    {
           tmp=m;
           m=n;
           n=tmp;
    }
    tmp=m%n;
    while(tmp!=0)
    {
                 m=n;
                 n=tmp;
                 tmp=m%n;
    }
    return n;
}

void display(int *pa)
{
     int i;
     printf("array:");
     for(i=0;i<Len;i++)
     printf("%d",pa[i]);
     printf("\n");
}

void swap(int *n1,int *n2)
{
     int tmp;
     tmp=*n1;
     *n1=*n2;
     *n2=tmp;
}

/**p����ָ�룬aLen:���ݳ��ȣ�k:��ѭ��λ��*/
void LeftRotation(int *p,int aLen,int k)
{
     int i,tmp,factor;
     k=k%aLen;
     if(k==0)return;
     k=aLen-k;
     factor=CommonFactor(aLen,k);
     if(factor==1)
     {
                  i=0;
                  do{
                      i=(i+k)%aLen;
                      swap(p,p+i);
                  }while(i!=0);
     }
     else{
          for(i=0;i<factor;i++)
          {
                               tmp=i;
                               do{
                                     tmp=(tmp+k)%aLen;
                                     swap(&p[i],p+tmp);
                               }while(tmp!=i);
          }
     }
} 

int main(int argc,char*argv[])
{
    int i,k,a[Len]={1,2,3,4,5,6,7,8};
    for(i=0;i<7;i++)
    {
                    for(k=0;k<Len;k++)//���鸳ֵ
                      a[k]=k+1;
                    k=i;
                    display(a);
                    printf("Len:%d,left rotation:%d\n",Len,k);
                    LeftRotation(a,Len,k);
                    display(a);
                    printf("----------------------\n"); 
    }
    system("pause");
    return 0;
}
