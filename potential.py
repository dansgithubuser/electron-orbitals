from constants import e_compute, epsilon_0_compute

import numpy as np

import math

def hydrogen_atom(shape, dx):
    v = np.zeros(shape, dtype=float)
    it = np.nditer(v, flags=['multi_index'])
    for _ in it:
        c = (np.array(shape) - np.ones(len(shape))) / 2
        r = np.array(it.multi_index) - c
        r = sum(r ** 2) ** (1/2)
        r *= dx
        v[it.multi_index] = -e_compute ** 2 / (4 * math.pi * epsilon_0_compute * r)
    return v
