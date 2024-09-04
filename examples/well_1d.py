import dansplotcore as dpc

from schrodinger import *

n = 100
shape = (n,)

v = np.zeros(shape, dtype=float)
v[  0] = 1
v[n-1] = 1

psi = np.zeros(shape, dtype=complex)
psi[3 * n // 4] = 1

hamiltonian = hamiltonian_single_particle(psi, v, m_e)

while True:
    dpc.plot(probability(psi), primitive=dpc.p.Line())
    evolve(psi, hamiltonian, 0.001)
