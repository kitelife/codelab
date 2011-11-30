/*移动内存算法
对于有K个元素的数组int a[K]={...}；写一个高效算法将数组内容循环左移m位。
比如：int a[6]={1,2,3,4,5,6},循环左移3位得到的结果{456123}
要求：
1.不允许另外申请数组空间，但可以申请少许变量；
2.不允许采用每次左移*/
#include<stdio.h>
#include<stdlib.h>
#define Len 8

/*求最大公约数的函数*/
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

/**p数据指针，aLen:数据长度，k:左循环位数*/
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
                    for(k=0;k<Len;k++)//数组赋值
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
