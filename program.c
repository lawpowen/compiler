#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#define CHMAXSIZE 100
FILE *fp;
char stack[CHMAXSIZE], ch, last_ch = '\0', last_op = '\0';
int now = 0, op_count = 0;

int main(int argc, char **argv)
{
    fp = fopen((argv[1], "r");
    if (fp == NULL)
        exit(0);
    ch = fgetc(fp);
    stack[now++] = ch;
    printf("I%c\n", ch);
    while ((ch = fgetc(fp)) != EOF)
    {
        if (isspace(ch) || ch == '\t')
            continue;
        last_ch = stack[now - 1];
        if (ch == 'i')
        {
            if (last_ch == '+' || last_ch == '*' || last_ch == '\0' || last_ch == '(')
            {
                printf("Ii\n");
                stack[now++] = ch;
            }
            else
            {
                printf("E\n");
                return 0;
            }
        }
        else if (ch == '+')
        {
            while (last_ch == '+' || last_ch == '*' || last_ch == 'i' || last_ch == ')')
            {
                printf("R\n");
                if (last_ch == ')')
                {
                    int here;
                    int i; 
                    for (i = now; i >= 0; i--)
                    {
                        if (stack[i] == '(')
                        {
                            here = i;
                            break;
                        }
                    }
                    int strl = strlen(stack);
                    for (i = here; i < strl; i++)
                    {
                        stack[i] = stack[i + 1];
                    }
                    now--;
                }
                now--;
                last_ch = stack[now - 1];
            }
            printf("I+\n");
            stack[now++] = ch;
        }
        else if (ch == '*')
        {
            while (last_ch == 'i' || last_ch == '*' || last_ch == ')')
            {
                printf("R\n");
                if (last_ch == ')')
                {
                    int here;
                    int i;
                    for (i = now; i >= 0; i--)
                    {
                        if (stack[i] == '(')
                        {
                            here = i;
                            break;
                        }
                    }
                    int strl = strlen(stack);
                    for (i = here; i < strl; i++)
                    {
                        stack[i] = stack[i + 1];
                    }
                    now--;
                }
                now--;
                last_ch = stack[now - 1];
            }
            printf("I*\n");
            stack[now++] = ch;
        }
        else if (ch == '(')
        {
            if (last_ch == '+' || last_ch == '*' || last_ch == '\0' || last_ch == '(')
            {
                printf("I(\n");
                stack[now++] = ch;
            }
            else
            {
                printf("E\n");
                return 0;
            }
        }
        else if (ch == ')')
        {
            if (last_ch == '+' || last_ch == '*')
            {
                printf("RE\n");
                return 0;
            }
            while (last_ch == '+' || last_ch == '*' || last_ch == ')' || last_ch == 'i')
            {

                printf("R\n");
                if (last_ch == ')')
                {
                    int here;
                    int i;
                    for (i = now; i >= 0; i--)
                    {
                        if (stack[i] == '(')
                        {
                            here = i;
                            break;
                        }
                    }
                    int strl = strlen(stack);
                    for (i = here; i < strl; i++)
                    {
                        stack[i] = stack[i + 1];
                    }
                    now--;
                }
                now--;
                last_ch = stack[now - 1];
            }
            printf("I)\n");
            stack[now++] = ch;
        }
    }
    last_ch = stack[now - 1];
    if (last_ch == ')')
    {
        int here;
        int i;
        for (i = now; i >= 0; i--)
        {
            if (stack[i] == '(')
            {
                here = i;
                break;
            }
        }
        int strl = strlen(stack);
        for (i = here; i < strl; i++)
        {
            stack[i] = stack[i + 1];
        }
        now--;
    }
    if (last_ch == '+' || last_ch == '*')
    {
        printf("RE\n");
        return 0;
    }
    int i;
    for (i = now - 1; i >= 0; i--)
    {
        if (stack[i] == '(')
        {
            printf("E\n");
            return 0;
        }
        printf("R\n");
    }
}
