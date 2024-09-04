import numpy as np

import math

h_bar = 6.62607015e-34 / (2 * math.pi)
m_e = 9.1093837139e-31

def laplacian(f):
    grad = np.gradient(f)
    if type(grad) != tuple: grad = (grad,)
    grad2 = []
    for i in range(len(grad)):
        grad2.append(np.gradient(grad[i], axis=i))
    return sum(grad2)

def potential_energy(psi, v):
    return v * psi

def kinetic_energy(psi, m):
    return -(h_bar ** 2 / (2 * m)) * laplacian(psi)

def hamiltonian_single_particle(psi, v, m):
    def hamiltonian(psi):
        return kinetic_energy(psi, m) + potential_energy(psi, v)
    return hamiltonian

def schrodinger(psi, hamiltonian):
    return hamiltonian(psi) / (1j * h_bar)

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
