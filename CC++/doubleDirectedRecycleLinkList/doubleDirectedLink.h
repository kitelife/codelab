#include <stdlib.h>

typedef struct node *nodePointer;
typedef int element;

struct node {
	element data;
	nodePointer llink;
	nodePointer rlink;
};

void initList(nodePointer header)
{
	header->data = 0;
	header->rlink = header;
	header->llink = header;
}

void dinsert(nodePointer node, nodePointer newnode)
{
	/* insert newnode to the right of node */
	newnode->llink = node;
	newnode->rlink = node->rlink;
	node->rlink->llink = newnode;
	node->rlink = newnode;
}

void ddelete(nodePointer node, nodePointer deleted)
{
	// delete from the doubly linked list
	if (node == deleted)
		printf("Deletion of header node not permitted.\n");
	else {
		deleted->llink->rlink = deleted->rlink;
		deleted->rlink->llink = deleted->llink;
		free(deleted);
	}
}
