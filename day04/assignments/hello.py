# write your program here
from mpi4py import MPI
COMM = MPI.COMM_WORLD
SIZE = COMM.Get_size()
RANK = COMM.Get_rank()
print('Hello from the rank {RANK} process'.format(RANK = RANK))
COMM.Barrier()
if RANK == 0:
   print('Parallel execution of hello_world with {SIZE}\n'.format(SIZE = SIZE))
