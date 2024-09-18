from schrodinger import *

import dansplotcore as dpc

import os
import math

h = os.environ.get('HARMONIC')

n = 100
shape = (n,)

v = np.zeros(shape, dtype=float)
v[n//10:9*n//10] = -2

psi = np.zeros(shape, dtype=complex)
psi[3*n//4] = 1

if h:
    psi[n//10:9*n//10] = np.sin(np.linspace(0, int(h)*math.pi, 8*n//10, dtype=complex))

hamiltonian = hamiltonian_single_particle(psi, v, 1, 1)

plot = dpc.Plot(primitive=dpc.p.LineComplexY())

class Updater:
    def __init__(self):
        self.psi = psi
        self(0)

    def __call__(self, dt):
        plot.clear()
        for _ in range(1000):
            self.psi = evolve(self.psi, hamiltonian, 0.001)
        plot.plot(probability(self.psi))
        plot.plot(self.psi)
        plot.plot(v)

plot.show(update=Updater())
