import dansplotcore as dpc

from schrodinger import *

import cmath
import math

m = 150
n = 150
wall_x = 40
slit_offset=10
slit_size=5
shape = (m, n)

v0 = 2
v = np.zeros(shape, dtype=float)
v[3:-3, 3:-3] = -v0  # well
v[wall_x-2:wall_x+2, :] = 0  # wall
a = slit_offset
b = slit_offset + slit_size
v[wall_x-2:wall_x+2, n//2-b:n//2-a] = -v0  # slit
v[wall_x-2:wall_x+2, n//2+a:n//2+b] = -v0  # slit

# Gaussian wave packet with momentum, 2D
psi = np.zeros(shape, dtype=complex)
packet_x = wall_x // 2
packet_y = n // 2
packet_r = 20
packet_w2 = 10 ** 2  # squared width
packet_p = 0.5  # momentum
for x in range(packet_x - packet_r, packet_x + packet_r + 1):
    for y in range(packet_y - packet_r, packet_y + packet_r + 1):
        d2 = (x - packet_x) ** 2 + (y - packet_y) ** 2
        psi[x, y] = np.exp(-d2 / packet_w2 + 1j * x * packet_p)

hamiltonian = hamiltonian_single_particle(psi, v, 1, 1)

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
            evolve(psi, hamiltonian, 0.001)
        i = 0
        z_max = np.max(np.abs(psi))
        for y, row in enumerate(psi):
            for x, z in enumerate(row):
                a = abs(z) / z_max
                phase = cmath.phase(z)
                r = (math.sin(phase + 0 * math.tau / 3) + 1) / 2
                g = (math.sin(phase + 1 * math.tau / 3) + 1) / 2
                b = (math.sin(phase + 2 * math.tau / 3) + 1) / 2
                i = plot.buffer.recolor(i, 6, r, g, b, a)
        plot.buffer.prep('dynamic')

plot.show(update=Updater(), update_reconstruct=False)
