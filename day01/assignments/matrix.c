#include<stdio.h>
#include<time.h>
#include <stdlib.h>

int main(){
  int max_stride = 20;
  int N = 100000,i_stride,i,j,k;
  double *x, *y, *z;
  double begin,end;
  x = (double *)malloc(max_stride * N * sizeof(double));
  y = (double *)malloc(max_stride * N * sizeof(double));
  z = (double *)malloc(max_stride * N * sizeof(double));
 
  double rat[25];
  double cpu[25];
  double mean, msec,rate;
  srand(time(NULL));
 
  for (i = 0; i < N * max_stride;i++){
  for (j = 0; i < N * max_stride;i++){
  x[i,j] = 1.0;
  y[i,j] = 1.0;
  z[i,j] = 0.0;
 }
    }
   
    for(i_stride = 1; i_stride <= max_stride; i_stride++)
    {
   begin =  (double) clock () / (double) CLOCKS_PER_SEC;
   
  for (i = 0; i < N * max_stride;i++){
  for (j = 0; i < N * max_stride;i++){
  for (k = 0; i < N * max_stride;i++){
  z[i,j] = z[i,j] + x[i,k]* y[k,j];
 }
 }
   }
   	
       end = (double) clock () / (double) CLOCKS_PER_SEC;
   	
       
       msec = (end - begin)* 1000;
       
       rate = 8 * N * (1000.0/msec) / (1024*1024);
       printf("-----------------------------------------\n\n");
       printf("i_stride = %d\nmean = %f\nCPU_Time = %f\nrate = %f\n",       i_stride,mean,msec,rate);
       rat[i_stride-1] = rate;
       cpu[i_stride-1] = msec;

    }
     // affichage des vecteurs rate et cpu pour chaque stride
     printf(" rate= [");
    for(i_stride = 1; i_stride <= max_stride; i_stride++){
    printf("%f,",rat[i_stride-1]);
   }
    printf("] cpu\n = [");
    for(i_stride = 1; i_stride <= max_stride; i_stride++){
    printf("%f,",cpu[i_stride-1]);
}
   printf("]");

   
    return 0;

}
