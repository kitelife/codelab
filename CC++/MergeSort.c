//********************************************************************
// Author: Xiayf
// Date: 2011/9/29
// What: Merge Sort
//********************************************************************
#include <stdio.h>
#include <stdlib.h>

void mergeSort(int *arrayToBeSorted, int start, int end);
void merge(int *arrayToBeSorted, int start, int middle, int end);

int main()
{
    int volume, index, data;
    printf("Please Input the Volume of Array to be Sorted:");
    scanf("%d",&volume);
    int arrayToBeSorted[volume];

    for(index = 0; index < volume; index++){
        scanf("%d",&data);
        arrayToBeSorted[index] = data;
    }

    mergeSort(arrayToBeSorted, 0, volume - 1);

    for(index = 0; index < volume; index ++){
        printf("%d\n", arrayToBeSorted[index]);
    }

    return 0;
}

void mergeSort(int *arrayToBeSorted, int start, int end){
    int middle;
    if(start < end){
        middle = (start + end) / 2;
        mergeSort(arrayToBeSorted, start, middle);
        mergeSort(arrayToBeSorted, middle + 1, end);
        merge(arrayToBeSorted, start, middle, end);
    }
}

void merge(int *arrayToBeSorted, int start, int middle, int end){
    int lenOfLeft, lenOfRight;
    lenOfLeft = middle - start + 1;
    lenOfRight = end - middle;

    int leftArray[lenOfLeft], rightArray[lenOfRight], index;
    for(index = 0; index < lenOfLeft; index ++)
        leftArray[index] = arrayToBeSorted[start + index];
    for(index = 0; index < lenOfRight; index ++)
        rightArray[index] = arrayToBeSorted[middle + index + 1];

    int leftIndex = 0, rightIndex = 0;
    for(index = start; index <= end; index ++){
        if(leftIndex == lenOfLeft){
            arrayToBeSorted[index] = rightArray[rightIndex];
            rightIndex++;
        }else if(rightIndex == lenOfRight){
            arrayToBeSorted[index] = leftArray[leftIndex];
            leftIndex++;
        }else if(leftArray[leftIndex] <= rightArray[rightIndex]){
            arrayToBeSorted[index] = leftArray[leftIndex];
            leftIndex++;
        }else{
            arrayToBeSorted[index] = rightArray[rightIndex];
            rightIndex ++;
        }
    }
}
