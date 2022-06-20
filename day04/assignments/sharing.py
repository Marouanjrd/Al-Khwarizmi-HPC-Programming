# write your program here
from mpi4py import MPI
COMM = MPI.COMM_WORLD
RANK = COMM.Get_rank()
SIZE = COMM.Get_size()
while True:
   if RANK == 0:
       sendbuf = int(input())
   else: 
       sendbuf = None    
   recv = COMM.bcast(sendbuf, root = 0)    
   print('Process {RANK} got {data}'.format(RANK = RANK, data = recv))   
   if recv < 0: break
