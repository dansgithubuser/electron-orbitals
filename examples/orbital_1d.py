import constants
import initial
import potential
from schrodinger import *

import dansplotcore as dpc
import numpy as np

import os
import math

h = int(os.environ.get('HARMONIC', 1))

n = 50
shape = (n,)
dx = (1/n) * constants.a_0_compute * 50

v = potential.hydrogen_atom(shape, dx)
psi = initial.hydrogen_wavefunction(shape, dx, h)
hamiltonian = hamiltonian_single_particle(psi, v, constants.m_e_compute, dx)

plot = dpc.Plot(primitive=dpc.p.LineComplexY())

class Updater:
    def __init__(self):
        self.psi = psi
        self(0)

    def __call__(self, dt):
        plot.clear()
        for _ in range(1000):
            self.psi = evolve(self.psi, hamiltonian, 1)
        plot.plot(probability(self.psi))
        plot.plot(self.psi)
        plot.plot(np.log10(abs(v)) / 10)
        log_prob = np.log10(probability(self.psi))
        plot.plot([
            (i, v / 10)
            for i, v in enumerate(log_prob)
            if v > -10
        ])

plot.show(update=Updater())
