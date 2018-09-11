#include<stdio.h>
int main(){
  int i,j,a=0,b[10],c[10],d[10];
  for(i=0;i<10;i++){
    scanf("%d %d",&c[i],&b[i]);
    for(j=0;j<10;j++){
      if(j%2)a+=i+j;
      d[j]=d[j-1]+b[i]+c[j]+a;
    }
  }
  printf("%d",a);
  return 0;
}
