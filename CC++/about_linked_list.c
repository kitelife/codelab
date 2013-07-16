//#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>       

typedef struct stud		//结构体定义
{
    char name[20];
    struct stud *llink, *rlink;
} stud;

stud* create(int n)	//创建链表函数定义
{
    stud * p = NULL, *h = NULL, *s = NULL;
    int i;
    for (i = 0; i < n; i++)
    {
        if ((s = (stud *)malloc(sizeof(stud))) == NULL)
            printf("error\n");
        else if (h == NULL)
	    {
	        printf("input name of %d: ", i + 1);
	        scanf("%s", s->name);
	  
	        //s->llink = h;
	        //s->rlink = p;
	        h = s;
	        h->llink = NULL;
	        h->rlink = NULL;
	        p = h;
	    }
        else
	    {
	        //p->rlink=s;
	        printf ("input name of %d: ", i + 1);
	        scanf("%s", s->name);
	        p->rlink = s;
	        s->llink = p;
	        s->rlink = NULL;
	        p = s;  
	        //h->llink=s;
	        //p->rlink=h;
	    }
    }
    //p->rlink=NULL;
    return h;
}

stud * search(stud * h, char *x)	//查询链表
{
    stud * p;
    char *y;
    p = h;
    while(p != NULL)
    {
        y = p->name;
        if (strcmp(y, x) == 0)
            return p;
        else
            p = p->rlink;
    }

    printf ("没有查找到该数据!");
    return NULL;
}

void print(stud * h)		//输出链表
{
    stud * p;
    p = h;
  
    //p=h->rlink;
    printf ("数据信息为：\n");
    while(p != NULL)
    {
        printf("%s", p->name);
        p = p->rlink;
        printf("\n");
    }
}

void insert (stud * p)		//插入
{
    char stuname[20];
    stud * s;
    if ((s = (stud *)malloc(sizeof(stud))) == NULL)
    {
        printf ("error");   
        exit (0);
    }
    else
    {
        printf("input the insert name: ");
        scanf("%s", stuname);
        strcpy(s->name, stuname);
        s->rlink = p->rlink;
        p->rlink = s;
        s->llink = p;
        (s->rlink)->llink = s;
    }
}

int main() 
{
    int num;
    stud * head, *searchpoint;
    char* studname = (char*)malloc(sizeof(char) * 20);
    
    printf("input your number: ");
    scanf("%d", &num);
    
    head = create(num);
    print(head);
    
    printf("请输入你要查找的人的姓名: ");
    scanf("%s", studname);
    
    searchpoint = search(head, studname);
    if (searchpoint != NULL)
    {
        printf("你所要查找的人的姓名是: %s\n", searchpoint->name);
        insert(searchpoint);
    }
    print(head);
    
    return 0;
}
