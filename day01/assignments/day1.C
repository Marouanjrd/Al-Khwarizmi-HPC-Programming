#include<stdio.h>
#include<time.h>
#include<stdlib.h>

int main ()
{

  int max_stride = 21, seed = 86456;
  int N = 100000, i_stride;
  double * a;
  a = (double *)malloc(max_stride * N * sizeof(double));
  double mean, msec, rate, begin,end;
  double rat[25];
  double cpu[25];
  srand(time(NULL));



  for (int i = 0; i < N * max_stride; i++)
    {
      a[i] = rand()%100 + 1.0;
    }

  for (i_stride = 1; i_stride < max_stride; i_stride++)
    {

      mean = 0.0;
      // temps de départ
       begin =  (double) clock () / (double) CLOCKS_PER_SEC;

      for (int i = 0; i < N * i_stride; i += i_stride)
  {
    mean = mean + a[i];
  }

      //temps de la fin de l'opération;
       end = (double) clock () / (double) CLOCKS_PER_SEC;
      // Cpu_Time
      msec = (end - begin) * 1000;
      // Bande_passante
      rate = 8 * N * (1000.0 / msec) / (1024 * 1024);
      printf ("-----------------------------------------\n\n");
      printf ("i_stride = %d \nmean = %f\nmsec = %f\nrate = %f\n",
        i_stride, mean, msec, rate);
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
