//***********************************************************************
// Author: Xiayf
// Date: 2011/9/29
// What: Insertion Sort
//***********************************************************************

#include <stdio.h>
#include <stdlib.h>

void insertionSort(int *intArray, int arrayVolume);

int main()
{
    int arrayVolume, index, data;
    printf("The Volume of Array:");
    scanf("%d",&arrayVolume);
    int arrayToBeSorted[arrayVolume];
    for(index = 0; index < arrayVolume; index++){
        scanf("%d",&data);
        arrayToBeSorted[index] = data;
    }
    insertionSort(arrayToBeSorted,arrayVolume);
    for(index = 0; index < arrayVolume; index++)
        printf("%d ",arrayToBeSorted[index]);
    printf("\n");
    return 0;
}

void insertionSort(int *intArray, int arrayVolume){
    int index, key, foreDataIndex;
    for(index = 1; index < arrayVolume; index ++){
        key = intArray[index];
        foreDataIndex = index - 1;
        while(foreDataIndex >= 0 && intArray[foreDataIndex] > key){
            intArray[foreDataIndex + 1] = intArray[foreDataIndex];
            foreDataIndex = foreDataIndex - 1;
        }
        intArray[foreDataIndex + 1] = key;
    }
}
