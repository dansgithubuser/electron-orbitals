import numpy as np

import math

h_bar = 6.62607015e-34 / (2 * math.pi)
m_e = 9.1093837139e-31

def mass_to_compute_units(m):
    return m / h_bar

def laplacian(f, dx):
    # let x = i * dx, so f[i] = f(x)
    # 1st derivative estimation: df(x) = (f(x+dx/2) - f(x-dx/2)) / dx
    # 2nd derivative estimation: d2f(x) = (df(x+dx/2) - df(x-dx/2)) / dx
    # = ((f(x+dx/2+dx/2) - f(x+dx/2-dx/2)) / dx - (f(x-dx/2+dx/2) - f(x-dx/2-dx/2)) / dx) / dx
    # = ((f(x+dx) - f(x)) / dx - (f(x) - f(x-dx)) / dx) / dx
    # = ((f(x+dx) - f(x)) - (f(x) - f(x-dx))) / dx ** 2
    # = (f(x+dx) - f(x) - f(x) + f(x-dx)) / dx ** 2
    # = (f(x+dx) - 2*f(x) + f(x-dx)) / dx ** 2
    kernel = np.array([1, -2, 1])
    n = len(f.shape)
    def kernel_shape(i):
        s = np.ones(n, dtype=int)
        s[i] = 3
        return s
    d2 = np.zeros_like(f)
    for i in range(n):
        d2 += np.convolve(f, kernel.reshape(kernel_shape(i)), mode='same')
    return d2 / dx ** 2

def potential_energy(psi, v):
    return v * psi

def kinetic_energy(psi, m, dx):
    return -(1 / (2 * m)) * laplacian(psi, dx)

def hamiltonian_single_particle(psi, v, m, dx):
    def hamiltonian(psi):
        return kinetic_energy(psi, m, dx) + potential_energy(psi, v)
    return hamiltonian

def schrodinger(psi, hamiltonian):
    return hamiltonian(psi) / 1j

def probability(psi):
    return np.absolute(psi) ** 2

def evolve(psi, hamiltonian, dt):
    psi += dt * schrodinger(psi, hamiltonian)
    # normalize
    # we seek total_probability = 1
    # probability /= total_probability
    # np.absolute(psi) ** 2 /= total_probability
    # psi /= total_probability ** (1/2)
    total_probability = np.sum(probability(psi))
    psi /= total_probability ** (1/2)
