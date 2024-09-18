from schrodinger import *
from initial import *

import dansplotcore as dpc

n = 200
shape = (n, n)

v = np.zeros(shape, dtype=float)
for i in range(n):
    for j in range(n):
        if i == j:
            v[i, j] = 2
        else:
            v[i, j] = 1 / abs(i - j)

psi = np.zeros(shape, dtype=complex)
psi[25:75, 125:175] = gaussian_wave_packet((50, 50), 1, 10, np.array([0.5, -0.5]))

hamiltonian = hamiltonian_multiple_particles_1d(psi, v, [1, 1], 1)

plot = dpc.Plot()
plot.plot_2d(probability(psi))

class Updater:
    def __init__(self):
        self.psi = psi

    def __call__(self, dt):
        for _ in range(10):
            self.psi = evolve(self.psi, hamiltonian, 0.01)
        i = 0
        z_max = np.max(np.abs(self.psi))
        for y, row in enumerate(self.psi):
            for x, z in enumerate(row):
                a = abs(z) / z_max
                phase = cmath.phase(z)
                r = (math.sin(phase + 0 * math.tau / 3) + 1) / 2
                g = (math.sin(phase + 1 * math.tau / 3) + 1) / 2
                b = (math.sin(phase + 2 * math.tau / 3) + 1) / 2
                i = plot.buffer.recolor(i, 6, r, g, b, a)
        plot.buffer.prep('dynamic')

plot.show(update=Updater(), update_reconstruct=False)
