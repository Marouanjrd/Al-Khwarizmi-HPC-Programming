# write your code here
@types('float[:,:]','float[:,:]','float[:,:]','float[:,:]','int','float','float','float')
def solve_2d_nonlinearconv_pure(u, un, v, vn, nt, dt, dx, dy):

    ###Assign initial conditions
    ##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
    u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
    ##set hat function I.C. : v(.5<=x<=1 && .5<=y<=1 ) is 2
    v[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
    row, col = u.shape
    
    #fill the update of u and v
    #$ omp parallel
    for n in range(nt):
        #$ omp for collapse(2)
        for i in range (row):
            for j in range(col):
                un[i,j] = u[i,j]
                vn[i,j] = v[i,j]
        #$ omp for collapse(2)
        for i in range(1, row-1):
            for j in range(1,col-1):
                u[i,j] = un[i,j] - (un[i,j] *( dt / dx) * (un[i,j] - un[i-1,j])) - (vn[i,j] * (dt / dy) * (un[i,j] - un[i,j-1]))
                v[i,j] = vn[i,j] - (un[i,j] * (dt / dx) * (vn[i,j] - vn[i-1,j])) -( vn[i,j] * (dt / dy) * (vn[i,j] - vn[i,j-1]))
    #$ omp end parallel
        
    return 0
if __name__ == "__main__" :
    
    import numpy as np
    
    ##variable declarations
    nx = 101
    ny = 101
    nt = 80
    #c = 1
    dx = 2 / (nx - 1)
    dy = 2 / (ny - 1)
    sigma = .2
    dt = sigma * dx


    u = np.ones((ny, nx)) ##create a 1xn vector of 1's
    v = np.ones((ny, nx))
    un = np.ones((ny, nx))
    vn = np.ones((ny, nx)) 
    
    # start CPU timing
    #import time
    #cpu_0 = time.process_time()
    #pyccelizing the function
    #from pyccel.epyccel import epyccel
    #solve_2d_nonlinearconv_f90 = epyccel(solve_2d_nonlinearconv_pyccel,)
    #execution
    solve_2d_nonlinearconv_pure(u, un, v, vn, nt, dt, dx, dy)
    # CPU time
    #cpu_1 = time.process_time()
    #cpu = cpu_1 - cpu_0
    #print("CPU time       :", cpu,        '\n')
