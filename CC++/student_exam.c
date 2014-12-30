
/*题目一：小学生测验
面向小学1~2年级学生，随机选择两个整数和加减法形成算式要求学生解答。
功能要求：
（1）电脑随机出10道题，每题10分，程序结束时显示学生得分；
（2）确保算式没有超出1~2年级的水平，只允许进行50以内的加减法，不允许两数之和或之差超出0~50的范围，负数更是不允许的；
（3）每道题学生有三次机会输入答案，当学生输入错误答案时，提醒学生重新输入，如果三次机会结束则输出正确答案；
（4）对于每道题，学生第一次输入正确答案得10分，第二次输入正确答案得7分，第三次输入正确答案得5分，否则不得分；
（5）总成绩90以上显示“SMART”
,80-90显示“GOOD”，70-80显示“OK”,60-70显示“PASS”，60以下“TRY AGAIN”。
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

    // 1 则用加法
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
    int table[] = {10, 7, 5}; // 第一次输入正确答案得10分，第二次输入正确答案得7分，第三次输入正确答案得5分

    for (i = 0; i < 3; i++)
    {
        printf("第 %d 机会，请输入结果：", i+1);
        scanf("%d", &answer);
        if (answer == result)
        {
            printf("回答正确！\n\n");
            return table[i];
        }
        printf("回答错误！\n");
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
        printf("第 %d 道题为", i+1);
        score += question();
    }
    printf("总分：%d, ", score);
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
