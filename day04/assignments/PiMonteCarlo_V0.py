# write your program here
import random 
import timeit
from mpi4py import MPI


COMM = MPI.COMM_WORLD
nbOfproc = COMM.Get_size()
RANK = COMM.Get_rank()

INTERVAL = 1000 ** 2
#Local interval for each proc
Local_int = INTERVAL //nbOfproc 
random.seed(42)  

def compute_points():
   
   random.seed(42)  
   
   circle_points= 0

   # Total Random numbers generated= possible x 
   # values* possible y values 
   for i in range(Local_int): 
     
       # Randomly generated x and y values from a 
       # uniform distribution 
       # Rannge of x and y values is -1 to 1 
               
       rand_x= random.uniform(-1, 1) 
       rand_y= random.uniform(-1, 1) 
     
       # Distance between (x, y) from the origin 
       origin_dist= rand_x**2 + rand_y**2
     
       # Checking if (x, y) lies inside the circle 
       if origin_dist<= 1: 
           circle_points+= 1
     
       # Estimating value of pi, 
       # pi= 4*(no. of points generated inside the  
       # circle)/ (no. of points generated inside the square) 
   
    
   
   return circle_points


start = timeit.default_timer()
circle_points = compute_points()
end = timeit.default_timer()

#Return the sum of all circle points to the process 0
circle_points = COMM.reduce(circle_points, op = MPI.SUM, root = 0)
if RANK == 0:
   pi = 4* circle_points/ INTERVAL
   print("Circle points number :",circle_points)
   print("Final Estimation of Pi=", pi, "cpu time :",(end-start) * 1000) 
