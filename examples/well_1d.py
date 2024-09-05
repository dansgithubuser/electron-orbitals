import dansplotcore as dpc

from schrodinger import *

n = 100
shape = (n,)

v = np.zeros(shape, dtype=float)
v[n//5:4*n//5] = -1

psi = np.zeros(shape, dtype=complex)
psi[3*n//5:4*n//5] = 1

hamiltonian = hamiltonian_single_particle(psi, v, 1)

plot = dpc.Plot(primitive=dpc.p.LineComplexY())

class Updater:
    def __init__(self):
        self(0)

    def __call__(self, dt):
        plot.clear()
        evolve(psi, hamiltonian, 0.1)
        plot.plot(probability(psi))
        plot.plot(psi)
        plot.plot(v)

plot.show(update=Updater())
