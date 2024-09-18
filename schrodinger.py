from constants import *

import numpy as np
from scipy.ndimage import laplace, shift

import math

def laplacian(f, dx):
    return laplace(f, mode='constant', cval=0) / dx ** 2

def double_derivative(f, dx, axis):
    # let x = i * dx, so f[i] = f(x)
    # 1st derivative estimation: df(x) = (f(x+dx/2) - f(x-dx/2)) / dx
    # 2nd derivative estimation: d2f(x) = (df(x+dx/2) - df(x-dx/2)) / dx
    # = ((f(x+dx/2+dx/2) - f(x+dx/2-dx/2)) / dx - (f(x-dx/2+dx/2) - f(x-dx/2-dx/2)) / dx) / dx
    # = ((f(x+dx) - f(x)) / dx - (f(x) - f(x-dx)) / dx) / dx
    # = ((f(x+dx) - f(x)) - (f(x) - f(x-dx))) / dx ** 2
    # = (f(x+dx) - f(x) - f(x) + f(x-dx)) / dx ** 2
    # = (f(x+dx) - 2*f(x) + f(x-dx)) / dx ** 2
    s = np.zeros(len(f.shape))
    s[axis] = 1
    a = shift(f, +s, order=0)
    b = shift(f, -s, order=0)
    return (a - 2*f + b) / dx ** 2

def potential_energy(psi, v):
    return v * psi

def kinetic_energy(psi, m, dx):
    return -(h_bar_compute ** 2 / (2 * m)) * laplacian(psi, dx)

def hamiltonian_single_particle(psi, v, m, dx):
    def hamiltonian(psi):
        return kinetic_energy(psi, m, dx) + potential_energy(psi, v)
    return hamiltonian

def hamiltonian_multiple_particles_1d(psi, v, ms, dx):
    def hamiltonian(psi):
        h = potential_energy(psi, v)
        for i, m in enumerate(ms):
            h += -(h_bar_compute ** 2 / (2 * m)) * double_derivative(psi, dx, i)
        return h
    return hamiltonian

def schrodinger(psi, hamiltonian):
    return hamiltonian(psi) / (1j * h_bar_compute)

def probability(psi):
    return np.absolute(psi) ** 2

def normalizing_factor(psi):
    # we seek total_probability = 1
    # probability /= total_probability
    # np.absolute(psi) ** 2 /= total_probability
    # psi /= total_probability ** (1/2)
    return np.sum(probability(psi)) ** (1/2)

def normalize(psi):
    return psi / normalizing_factor(psi)

def normalize_in_place(psi):
    psi /= normalizing_factor(psi)

def evolve(psi, hamiltonian, dt):
    psi += dt * schrodinger(psi, hamiltonian)
    return normalize(psi)
