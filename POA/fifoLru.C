#include <stdio.h>
int n=10, nf=3;
int in[]={4, 7, 6, 1, 7, 6, 1, 2, 7, 2};
int p[50];
int hit = 0;
int i, j, k;
int pgfaultcnt = 0;
void initialize()
{
    pgfaultcnt = 0;
    for (i = 0; i < nf; i++)
        p[i] = 9999;
}

int isHit(int data)
{
    hit = 0;
    for (j = 0; j < nf; j++)
    {
        if (p[j] == data)
        {
            hit = 1;
            break;
        }
    }
    return hit;
}
int getHitIndex(int data)
{
    int hitind;
    for (k = 0; k < nf; k++)
    {
        if (p[k] == data)
        {
            hitind = k;
            break;
        }
    }
    return hitind;
}
void dispPages()
{
    for (k = 0; k < nf; k++)
    {
        if (p[k] != 9999)
            printf(" %d", p[k]);
    }
}

void dispPgFaultCnt()
{
    printf("\nTotal no of page faults:%d", pgfaultcnt);
}

void fifo()
{
    initialize();
    for (i = 0; i < n; i++)
    {
        printf("\nFor %d :", in[i]);
        if (isHit(in[i]) == 0)
        {
            for (k = 0; k < nf - 1; k++)
            p[k] = p[k + 1];
            p[k] = in[i];
            pgfaultcnt++;
            dispPages();
        }
        else
            printf("HIT");
    }
    dispPgFaultCnt();
}


void lru()
{
    initialize();
    int least[50];
    for (i = 0; i < n; i++)
    {
        printf("\nFor %d :", in[i]);
        if (isHit(in[i]) == 0)
        {
            for (j = 0; j < nf; j++)
            {
                int pg = p[j];
                int found = 0;
                for (k = i - 1; k >= 0; k--)
                {
                    if (pg == in[k])
                    {
                        least[j] = k;
                        found = 1;
                        break;
                    }
                    else
                        found = 0;
                }
                if (!found)
                    least[j] = -9999;
            }
            int min = 9999;
            int repindex;
            for (j = 0; j < nf; j++)
            {
                if (least[j] < min)
                {
                    min = least[j];
                    repindex = j;
                }
            }
            p[repindex] = in[i];
            pgfaultcnt++;
            dispPages();
        }
        else
            printf("HIT");
    }
    dispPgFaultCnt();
}


int main()
{
    int choice;
    while (1)
    {
        printf("\nPage Replacement Algorithms\n1.FIFO\n2.LRU\n3.Exit\nEnter your choice:");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            fifo();
            break;
        case 2:
            lru();
            break;
        default:
            return 0;
            break;
        }
    }
}
