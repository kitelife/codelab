
/*��Ŀһ��Сѧ������
����Сѧ1~2�꼶ѧ�������ѡ�����������ͼӼ����γ���ʽҪ��ѧ�����
����Ҫ��
��1�����������10���⣬ÿ��10�֣��������ʱ��ʾѧ���÷֣�
��2��ȷ����ʽû�г���1~2�꼶��ˮƽ��ֻ�������50���ڵļӼ���������������֮�ͻ�֮���0~50�ķ�Χ���������ǲ�����ģ�
��3��ÿ����ѧ�������λ�������𰸣���ѧ����������ʱ������ѧ���������룬������λ�������������ȷ�𰸣�
��4������ÿ���⣬ѧ����һ��������ȷ�𰸵�10�֣��ڶ���������ȷ�𰸵�7�֣�������������ȷ�𰸵�5�֣����򲻵÷֣�
��5���ܳɼ�90������ʾ��SMART��
,80-90��ʾ��GOOD����70-80��ʾ��OK��,60-70��ʾ��PASS����60���¡�TRY AGAIN����
*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

// a + b = c
// a <= 50, b <= 50, c <= 50
void rand3(int *a, int *b, int *c)
{
    *c = rand() % 50 + 1;
    *a = *c * ((float)rand() / RAND_MAX); // a divde
    *b = *c - *a;
}

int question()
{
    int result, answer, i;
    int a, b, c;
    rand3(&a, &b, &c);

    // 1 ���üӷ�
    if (rand() % 2)
    {
        printf("%d + %d = ?\n", a, b);
        result = c;
    }
    else
    {
        printf("%d - %d = ?\n", c, a);
        result = b;
    }
    int table[] = {10, 7, 5}; // ��һ��������ȷ�𰸵�10�֣��ڶ���������ȷ�𰸵�7�֣�������������ȷ�𰸵�5��

    for (i = 0; i < 3; i++)
    {
        printf("�� %d ���ᣬ����������", i+1);
        scanf("%d", &answer);
        if (answer == result)
        {
            printf("�ش���ȷ��\n\n");
            return table[i];
        }
        printf("�ش����\n");
    }
    printf("\n");
    return 0;
}

int main()
{
    srand(time(NULL));
    int i, r=1, score=0, round = 1, index = 7;
    for (i = 0; i < 10; i++)
    {
        printf("�� %d ����Ϊ", i+1);
        score += question();
    }
    printf("�ܷ֣�%d, ", score);
    switch (score / 10)
    {
    case 10:
        printf("SMART!\n");
        break;
    case 9:
        printf("SMART!\n");
        break;
    case 8:
        printf("GOOD!\n");
        break;
    case 7:
        printf("OK!\n");
        break;
    case 6:
        printf("PASS!\n");
        break;
    default:
        printf("TRY AGAIN!\n");
    }
    system("pause");
    return 0;
}
