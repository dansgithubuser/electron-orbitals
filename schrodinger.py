from constants import *

import numpy as np
from scipy.ndimage import laplace

import math

def laplacian(f, dx):
    return laplace(f, mode='constant', cval=0) / dx ** 2

def potential_energy(psi, v):
    return v * psi

def kinetic_energy(psi, m, dx):
    return -(h_bar_compute ** 2 / (2 * m)) * laplacian(psi, dx)

def hamiltonian_single_particle(psi, v, m, dx):
    def hamiltonian(psi):
        return kinetic_energy(psi, m, dx) + potential_energy(psi, v)
    return hamiltonian

def schrodinger(psi, hamiltonian):
    return hamiltonian(psi) / (1j * h_bar_compute)

def probability(psi):
    return np.absolute(psi) ** 2

def normalize(psi):
    # we seek total_probability = 1
    # probability /= total_probability
    # np.absolute(psi) ** 2 /= total_probability
    # psi /= total_probability ** (1/2)
    return psi / np.sum(probability(psi)) ** (1/2)

def evolve(psi, hamiltonian, dt):
    psi += dt * schrodinger(psi, hamiltonian)
    return normalize(psi)
