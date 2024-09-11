import initial

import dansplotcore as dpc
import numpy as np

import cmath
import math
import os

l = int(os.environ.get('l', 0))
m = int(os.environ.get('m', 0))

x = np.zeros((100, 50), dtype=complex)
for i, phi in enumerate(np.linspace(0, math.tau, x.shape[0])):
    for j, theta in enumerate(np.linspace(0, math.pi, x.shape[1])):
        x[i, j] = initial.spherical_harmonic(l, m, theta, phi)

plot = dpc.Plot(title=f'l={l} m={m}')
w = math.tau / x.shape[0]
h = math.pi / x.shape[1]
x_max = np.max(np.abs(x))
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        a = abs(x[i, j]) / x_max
        phase = cmath.phase(x[i, j])
        r = (math.sin(phase + 0 * math.tau / 3) + 1) / 2
        g = (math.sin(phase + 1 * math.tau / 3) + 1) / 2
        b = (math.sin(phase + 2 * math.tau / 3) + 1) / 2
        phi = i * w
        theta = j * h
        plot.rect(phi, theta, phi+w, theta+h, r, g, b, a)
plot.show()
