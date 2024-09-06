import numpy as np
from scipy.ndimage import laplace

import math

h_bar = 6.62607015e-34 / (2 * math.pi)
m_e = 9.1093837139e-31

def mass_to_compute_units(m):
    return m / h_bar

def laplacian(f, dx):
    return laplace(f) / dx ** 2

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
