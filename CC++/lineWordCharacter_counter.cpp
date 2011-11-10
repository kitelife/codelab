#include <stdio.h>
#include <stdlib.h>

#define IN 1
#define OUT 0

int main()
{
    int character=0, word=0, line=0,state=OUT;
    char c;
    FILE *fpForInput = fopen("input.txt","r");
    if(!fpForInput){
        printf("Can not open the file, maybe it's not exsist!\n");
        return 1;
    }
    while((c=fgetc(fpForInput))!=EOF)
    {
        if(c == '\n')
            line++;
        if(c == ' ' || c == '\n' || c == '\t')
            state = OUT;
        else if(state==OUT){
            state = IN;
            word++;
            character++;
        }
        else{
            character++;
        }
    }
    fclose(fpForInput);

    printf("character:%d\n",character);
    printf("word:%d\n",word);
    printf("line:%d\n",line);
    return 0;
}
