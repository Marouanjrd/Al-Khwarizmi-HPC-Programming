from mpi4py import MPI
COMM = MPI.COMM_WORLD
RANK = COMM.Get_rank()
SIZE = COMM.Get_size()
tag = 100
if RANK == 0:
    sendbuf = int(input())    
    COMM.send(sendbuf, dest = RANK + 1, tag = tag)
else:
    recvbuf = COMM.recv(source = RANK - 1, tag = tag)
    print('I, process',RANK,',I received',recvbuf,'from the process',RANK-1)
    if RANK != SIZE - 1:
        COMM.send(recvbuf,dest = (RANK + 1)%SIZE, tag = tag)   
