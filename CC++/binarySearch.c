/*
 * binarySearch.c
 *
 *  Created on: 2011-5-31
 *      Author: xyf
 */
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define random(x) (rand()%x)

int* binarySearch(int *header, int number, int object) {
	int low = 0, high = number - 1;
	while (low <= high) {
		int mid = (low + high) / 2;
		if (object == *(header + mid))
			return header + mid;
		else if (object < *(header + mid)) {
			high = mid - 1;
		} else
			low = mid + 1;
	}
	return NULL;
}
int main() {
	int num = 0, i = 0;
	int array[8] = { 0, 2, 3, 4, 5, 6, 7, 9 };
	num = sizeof(array) / sizeof(int);
	//printf("number = %d\n", num);

	srand((int)time(0));  //为rand()提供不同的seed

	while (i < 50) {
		int obj = random(15);
		printf("obj = %d\n",obj);
		int* pointer = binarySearch(array, num, obj);
		if (pointer == NULL)
			printf("There is no such object-number!\n");
		else
			printf("The object-number is %d\n", *pointer);
		i++;
	}
	return 0;
}
