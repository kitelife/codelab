//*************************************************************************
// Author: Xiayf
// Date: 2011/9/27
// What: Recursive solution to tower of Hanoi, based on stack.
//*************************************************************************

#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

int hanoi (int n, struct SqStack *x, struct SqStack *y, struct SqStack *z);

int main()
{
    int count=0, element=0, stepCount=0;
    struct SqStack A, B, C;
    InitStack(&A,"A");
    InitStack(&B,"B");
    InitStack(&C,"C");

    printf("Please Input the Number of Disks: ");
    scanf("%d",&count);
    int disk = count;

    while(disk > 0){
        Push(&A, disk);
        disk --;
    }

    stepCount = hanoi(count, &A, &B, &C);
    printf("StepCount: %d\n\n", stepCount);
    printf("Disks on C:\n");
    while(count > 0){
        printf("%d\n",Pop(&C));
        count --;
    }
    return 0;
}

int hanoi (int n, struct SqStack *x, struct SqStack *y, struct SqStack *z){
    int disk = 0, stepCount = 0, temp;
    if (n == 1){
        disk = Pop(x);
        Push(z, disk);
        printf("move %d from %s to %s\n",disk,x->name,z->name);
        stepCount ++;
    }else {
        temp = hanoi(n-1, x, z, y);
        disk = Pop(x);
        Push(z, disk);
        printf("move %d from %s to %s\n",disk, x->name, z->name);
        temp ++;
        stepCount = hanoi(n-1, y, x, z) + temp;
    }
    return stepCount;
}
