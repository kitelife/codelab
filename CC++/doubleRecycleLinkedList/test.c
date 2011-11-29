#include <stdio.h>
#include <stdlib.h>
#include "doubleRecycleLink.h"

int main()
{
	int index, data[5]={10,2,11,100,30};
	
	nodePointer listHeader, next;
	
	listHeader = (nodePointer)malloc(sizeof(struct node));
	initList(listHeader);
	
	int dataLength = sizeof(data)/sizeof(int);
	
	for(index = 0; index < dataLength; index++)
	{
		nodePointer tempnode = (nodePointer)malloc(sizeof(struct node));
		tempnode->data = data[index];
		dinsert(listHeader,tempnode);		
	}
	
	for(next = listHeader->rlink; next != listHeader; next = next->rlink)
	{
		printf("%d\n",next->data);
	}
	while(listHeader->rlink != listHeader)
	{
		ddelete(listHeader,listHeader->rlink);
	}
	free(listHeader);
	return 0;
}
