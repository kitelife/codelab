//矩阵转置的两种思路
//2012.4.1
#include <stdio.h>
#define M 5
void transpose(int (*)[M]);
void transpose2(int (*)[M]);
int main()
{
	int array[5][5]={{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};
	transpose(array);
	int i, j;
	for(i = 0; i < 5; i++){
		for(j = 0; j < 5; j++)
			printf("%2d ",array[i][j]);
		printf("\n");
	}
	printf("\n");
	transpose2(array);
	int k, p;
	for(k = 0; k < 5; k++){
		for(p = 0; p < 5; p++)
			printf("%2d ", array[k][p]);
		printf("\n");
	}
	printf("\n");
	return 0;
}

void transpose(int (*A)[M])
{
	int i, j;
	for(i = 0; i < M; i++)
		for(j = 0; j < i; j++){
			int t = A[i][j];
			A[i][j] = A[j][i];
			A[j][i] = t;
		}
}

void transpose2(int (*A)[M])
{
	int i, j;
	for(i = 0, j = 0; i < (M-1); i++, j++){
		int *p = &A[j][i];
		int t;
		while(j < M){
			t = A[i][j];
			A[i][j] = *p;
			*p = t;
			j++;
			p += M;
		}
		j = i;
	}
}
