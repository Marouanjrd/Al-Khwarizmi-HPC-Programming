from pyccel.stdlib.internal.openmp import omp_set_num_threads, omp_set_dynamic
from pyccel.decorators import types
from pyccel.stdlib.internal.openmp import omp_set_num_threads, omp_get_num_threads, omp_get_thread_num
import numpy as np

@types('int','int')
def pro_mat_collaps(M,N):
    
    
    print ("N = ", N,"  M = ", M,"\n" )
    
    A = np.empty((M, N))
    B = np.empty((N, M))
    C = np.empty((M, M))
    
    
    #$ omp parallel
    #$ omp for collapse(2)
    for i in range(M):
        for j in range(N):
            A[ i, j ] = (i + 1) + (j + 1)
    #$ omp end parallel
    

    #$ omp parallel
    #$ omp for collapse(2)
    for i in range(N):
        for j in range(M):
            B[ i, j ] = (i + 1) - (j + 1)
    #$ omp end parallel

    #$ omp parallel
    #$ omp for collapse(2)
    for i in range( M ):
        for j in range( M ):
            C[ i, j ] = 0
    #$ omp end parallel

    
    #$ omp parallel
    #$ omp for collapse (2)
    for i in range( M ):
        for j in range( M ):
            for k in range( N ):
                C[ i, j ] += A[ i, k ] * B[ k, j ]
    result = omp_get_num_threads()
    #$ omp end parallel
   
    return result

if __name__ == "__main__" :

    M = 20
    N = 20
    # Declare Matrices

    x = pro_mat_collaps(M,N)
    print("Execution of Matrix production in parallele with  ",x , "threads\n\n")
