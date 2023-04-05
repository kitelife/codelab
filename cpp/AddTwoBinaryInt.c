//*********************************************************************
// Author:œƒ”¿∑Ê
// Date: 2011/9/26
// What: Input two integers, transform to binary form, then add
//       the two binary integers, achives a binary sum integer,
//       then transform to the decimal form, print out some values.
//*********************************************************************

#include <stdio.h>
#include <stdlib.h>

int decimalToBinary(int decimal, int* array);

int main()
{

    int first = 0, second = 0, decimalSum = 0, index, firstToArray[32], secondToArray[32];
    printf("Please Input Two integers:");
    scanf("%d %d", &first, &second);
    printf("%d\n", first + second);

    int lenOfFirstToArray = decimalToBinary(first, firstToArray);
    printf("%d\n",lenOfFirstToArray);
    int lenOfSecondToArray = decimalToBinary(second, secondToArray);
    printf("%d\n",lenOfSecondToArray);

    int arrayInitLen = lenOfFirstToArray > lenOfSecondToArray ? lenOfFirstToArray : lenOfSecondToArray;

    int beforeAdder[arrayInitLen], afterAdder[arrayInitLen], sum[arrayInitLen + 1];
    for (index = 0; index < arrayInitLen; index++){
        beforeAdder[index] = 0;
        afterAdder[index] = 0;
        sum[index] = 0;
    }
    sum[arrayInitLen] = 0;

    for(index = 0; index < lenOfFirstToArray; index++)
        beforeAdder[index] = firstToArray[index];
        //afterAdder[index] = secondToArray[index];
    for(index = 0; index < lenOfSecondToArray; index++)
        afterAdder[index] = secondToArray[index];

    /*
    for (index = arrayInitLen - 1; index >= 0; index --){
        printf("%d",beforeAdder[index]);
    }
    printf("\n");
    for (index = arrayInitLen - 1; index >= 0; index --){
        printf("%d",afterAdder[index]);
    }
    printf("\n");
    */

    int carry = 0;
    int bitSum = 0;
    for(index = 0; index < arrayInitLen; index ++){
        bitSum = beforeAdder[index] + afterAdder[index] + carry;
        carry = bitSum / 2;       //Ω¯Œª
        sum[index] = bitSum % 2;
    }
    sum[arrayInitLen] = carry;

    for(index = arrayInitLen; index >= 0; index--){
        printf("%d",sum[index]);
        decimalSum = sum[index] + 2 * decimalSum;
    }
    printf("\n");
    printf("%d",decimalSum);

    return 0;
}

int decimalToBinary(int decimal, int* array)
{
    int index = 0;
    while(decimal !=0){
        array[index] = decimal % 2;
        decimal = decimal / 2;
        index ++;
    }
    return index;
}
