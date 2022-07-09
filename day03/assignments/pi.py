from pyccel.decorators import types

@types('int')
def pi(n):

    h = float(1/n)
    for k in range(100):
        Pi_calcul = 0.
        for i in range(n):
            x = h * (i + 0.5)
            Pi_calcul += 4.0 / (1. + x * x)


        Pi_calcul = h * Pi_calcul
    return Pi_calcul
