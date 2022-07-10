
from pyccel.stdlib.internal.openmp import omp_get_thread_num
from pyccel.decorators import types


def initialize_table(tab, nmolec, n, nmol):
    # Initialisation du tableau
    # First-touch pour garantir un fonctionnement optimal sur les systemes NUMA
    for k in range(nmolec):
        for j in range(n):
            for i in range(nmol):
                tab[ i,j,k ] = i + j + k


def reduction(tab:'float [:,:]', tab1 : 'float [:]', tab2 : 'float [:]', nmolec :'int', nmol:'int', n:'int'):
    for k in range(nmolec):
        tab1[:nmol] = 0
        for j in range(n):
            for i in range(nmol):
                tab1[i] = tab1[i] + tab[i,j,k]
        tab2[:nmol] = tab2[:nmol] + 2 * tab1[:nmol]

