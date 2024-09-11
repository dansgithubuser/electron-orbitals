from schrodinger import *

import dansplotcore as dpc

import cmath
import math

m = 200
n = 200
shape = (m, n)

v = np.zeros(shape, dtype=float)

# Gaussian wave packet with momentum, 2D
psi = np.zeros(shape, dtype=complex)
packet_x = 70
packet_y = 100
packet_r = 60
packet_w2 = 20 ** 2  # squared width
packet_p = 0.5  # momentum
for x in range(packet_x - packet_r, packet_x + packet_r + 1):
    for y in range(packet_y - packet_r, packet_y + packet_r + 1):
        d2 = (x - packet_x) ** 2 + (y - packet_y) ** 2
        psi[x, y] = np.exp(-d2 / packet_w2 + 1j * x * packet_p)

hamiltonian = hamiltonian_single_particle(psi, v, 1, 1)

plot = dpc.Plot()
plot.plot_2d(probability(psi))

class Updater:
    def __init__(self):
        self.psi = psi

    def __call__(self, dt):
        for _ in range(100):
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
