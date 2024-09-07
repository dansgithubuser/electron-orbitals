import dansplotcore as dpc

from schrodinger import *

import os
import math

m = 35 * 3
n = 65 * 3
wall_x = 10
slit_offset=9
slit_size=3
shape = (m, n)

v0 = 100
v = np.zeros(shape, dtype=float)
v[3:-3, 3:-3] = -v0  # well
v[wall_x-2:wall_x+2, :] = 0  # wall
a = slit_offset
b = slit_offset + slit_size
v[wall_x-2:wall_x+2, n//2-b:n//2-a] = -v0  # slit
v[wall_x-2:wall_x+2, n//2+a:n//2+b] = -v0  # slit

psi = np.zeros(shape, dtype=complex)

hamiltonian = hamiltonian_single_particle(psi, v, 0.1, 1)

plot = dpc.Plot(transform=dpc.t.Colors([
    dpc.t.Color.w,
    dpc.t.Color(0.0, 1.0, 0.0, 0.5),
    dpc.t.Color(1.0, 0.0, 0.0, 0.5),
    dpc.t.Color(0.0, 0.0, 1.0, 0.5),
]))
plot.plot_2d(probability(psi))
plot.plot_2d(v)

class Updater:
    def __call__(self, dt):
        for _ in range(100):
            for x in range(3, 6):
                for y in range(n):
                    r = y - n//2
                    z = x - m//7
                    k = 0.25
                    psi[x, y] = 1e-2 * np.exp(-r ** 2 / 1e2) * np.exp(-1j * (k * z))
            evolve(psi, hamiltonian, 0.01)
        i = 0
        p = probability(psi)
        z_max = np.max(p)
        for y, row in enumerate(p):
            for x, z in enumerate(row):
                w = z / z_max
                i = plot.buffer.recolor(i, 6, w, w, w, 1.0)
        plot.buffer.prep('dynamic')

plot.show(update=Updater(), update_reconstruct=False)
