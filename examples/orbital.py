import constants
import initial
import potential
from schrodinger import *

import dansplotcore as dpc
import numpy as np

import os
import cmath
import math

n = int(os.environ.get('n', 1))
l = int(os.environ.get('l', 0))
m = int(os.environ.get('m', 0))
axis = os.environ.get('axis', 'z')
tomograph = int(os.environ.get('tomograph', 0))
assert axis in ['x', 'y', 'z']

size = 50
shape = (size, size, size)
dx = (1/size) * constants.a_0_compute * 50

v = potential.hydrogen_atom(shape, dx)
psi = initial.hydrogen_wavefunction(shape, dx, n, l, m)
hamiltonian = hamiltonian_single_particle(psi, v, constants.m_e_compute, dx)

def plot_cut(psi, t):
    if axis == 'x':
        return psi[t, :, :]
    if axis == 'y':
        return psi[:, t, :]
    if axis == 'z':
        return psi[:, :, t]

plot = dpc.Plot(title=f'n={n} l={l} m={m}')
plot.plot_2d(probability(plot_cut(psi, 0)))

class Updater:
    def __init__(self):
        self.psi = psi
        self.t = size // 2

    def __call__(self, dt):
        for _ in range(10):
            self.psi = evolve(self.psi, hamiltonian, 100)
        i = 0
        cut = plot_cut(self.psi, self.t)
        if tomograph:
            self.t += 1
            if self.t == size:
                self.t = 0
        log_z_max = math.log10(np.max(np.abs(self.psi)))
        for y, row in enumerate(cut):
            for x, z in enumerate(row):
                a = max(1 + (math.log10(abs(z)) - log_z_max), 0)
                phase = cmath.phase(z)
                r = (math.sin(phase + 0 * math.tau / 3) + 1) / 2
                g = (math.sin(phase + 1 * math.tau / 3) + 1) / 2
                b = (math.sin(phase + 2 * math.tau / 3) + 1) / 2
                i = plot.buffer.recolor(i, 6, r, g, b, a)
        plot.buffer.prep('dynamic')

plot.show(update=Updater(), update_reconstruct=False)
