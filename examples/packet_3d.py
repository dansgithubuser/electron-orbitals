from schrodinger import *

import dansplotcore as dpc

import cmath
import math

size_x = 200
size_y = 100
size_z = 100
shape = (size_x, size_y, size_z)

v = np.zeros(shape, dtype=float)

# Gaussian wave packet with momentum, 3D
psi = np.zeros(shape, dtype=complex)
packet_x = 50
packet_y = 50
packet_z = 50
packet_r = 49
packet_w2 = 10 ** 2  # squared width
packet_p = 0.5  # momentum
for x in range(packet_x - packet_r, packet_x + packet_r + 1):
    for y in range(packet_y - packet_r, packet_y + packet_r + 1):
        for z in range(packet_z - packet_r, packet_z + packet_r + 1):
            d2 = (x - packet_x) ** 2 + (y - packet_y) ** 2 + (z - packet_z) ** 2
            psi[x, y, z] = np.exp(-d2 / packet_w2 + 1j * x * packet_p)

hamiltonian = hamiltonian_single_particle(psi, v, 1, 1)

plot = dpc.Plot()
plot.plot_2d(probability(psi[:, :, size_z // 2]))

class Updater:
    def __init__(self):
        self.psi = psi

    def __call__(self, dt):
        for _ in range(10):
            self.psi = evolve(self.psi, hamiltonian, 0.1)
        i = 0
        psi2 = self.psi[:, :, size_z // 2]
        z_max = np.max(np.abs(psi2))
        for y, row in enumerate(psi2):
            for x, z in enumerate(row):
                a = abs(z) / z_max
                phase = cmath.phase(z)
                r = (math.sin(phase + 0 * math.tau / 3) + 1) / 2
                g = (math.sin(phase + 1 * math.tau / 3) + 1) / 2
                b = (math.sin(phase + 2 * math.tau / 3) + 1) / 2
                i = plot.buffer.recolor(i, 6, r, g, b, a)
        plot.buffer.prep('dynamic')

plot.show(update=Updater(), update_reconstruct=False)
