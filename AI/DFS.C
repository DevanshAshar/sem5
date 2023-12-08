#include<stdio.h>
int a[100][100];
int v[100],n;
void DFS(int i)
{
    v[i]=1;
    printf("%d ",i);
    for(int j=0;j<n;j++)
    {
        if(a[i][j]==1 && v[j]==0)
        DFS(j);
    }
}
void main()
{
    int i,j;
    printf("Enter size of matrix ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("Enter 0/1 for (%d,%d) ",i,j);
            scanf("%d",&a[i][j]);
        }    
    }
    for(i=0;i<n;i++)
    v[i]=0;
    printf("\nAdjacency Matrix\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%d ",a[i][j]);
        }    
        printf("\n");
    }
    printf("enter vertex ");
    scanf("%d",&i);
    DFS(i);
}
