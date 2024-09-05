import dansplotcore as dpc

from schrodinger import *

n = 100
shape = (n,)

v = np.zeros(shape, dtype=float)
v[n//5:4*n//5] = -1

psi = np.zeros(shape, dtype=complex)
psi[3*n//4] = 1

hamiltonian = hamiltonian_single_particle(psi, v, 1)

while True:
    plot = dpc.Plot(primitive=dpc.p.LineComplexY())
    plot.plot(psi)
    plot.plot(v)
    plot.show()
    evolve(psi, hamiltonian, 1)
