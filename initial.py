import numpy as np

import cmath
import math

from constants import a_0_compute
from schrodinger import normalize

def fac(x):
    return math.factorial(x)

def hydrogen_calculate_a_k(k, n, l):
    if k == 0: return 1  # we normalize at the end anyhow
    return (k + l - n) / (k * (k + 2 * l + 1)) * hydrogen_calculate_a_k(k-1, n, l)

def hydrogen_radial_wavefunction(n, l, r):
    psi = 0
    rho = 2 * r / (n * a_0_compute)
    for k in range(n - l):
        a_k = hydrogen_calculate_a_k(k, n, l)
        psi += a_k * rho ** k
    psi *= math.exp(-rho/2) * rho ** l
    return psi

def associated_legendre_polynomial(l, m, x):
    if m == 0 and l == 0:
        return 1
    if m == l:
        return (-1) ** l * fac(fac(2 * l - 1)) * (1 - x ** 2) ** (l / 2)
    if l - m == 1:
        return x * (2 * m + 1) * associated_legendre_polynomial(m, m, x)
    if m < 0:
        return (-1) ** m * fac(l - m) / fac(l + m) * associated_legendre_polynomial(l, -m, x)
    a = x * (2*l - 1) * associated_legendre_polynomial(l-1, m, x)
    b = (l + m - 1) * associated_legendre_polynomial(l-2, m, x)
    return (a - b) / (l - m)

def spherical_harmonic(l, m, theta, phi):
    return associated_legendre_polynomial(l, m, math.cos(theta)) * cmath.exp(1j * m * phi)

def hydrogen_wavefunction(shape, dx, n, l=0, m=0):
    if l >= n:
        print('note: l should be less than n')
    if abs(m) > l:
        print('note: abs(m) should be less than or equal to l')
    psi = np.zeros(shape, dtype=complex)
    it = np.nditer(psi, flags=['multi_index'])
    for _ in it:
        c = (np.array(shape) - np.ones(len(shape))) / 2
        x, y, z = (np.array(it.multi_index) - c) * dx
        r = (x ** 2 + y ** 2 + z ** 2) ** (1/2)
        psi[it.multi_index] = hydrogen_radial_wavefunction(n, l, r)
        if len(shape) == 3:
            theta = math.acos(z / r)
            phi = math.acos(x / (x ** 2 + y ** 2) ** (1/2))
            if y < 0: phi *= -1
            psi[it.multi_index] *= spherical_harmonic(l, m, theta, phi)
    psi = normalize(psi)
    return psi
