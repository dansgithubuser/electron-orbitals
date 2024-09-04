# Schrodinger's Equation
Schrodinger's equation comes in a few forms. We're interested in the "time-dependent" form, which is the general form. We'll split this equation into three parts:
- a wave function
- a Hamiltonian operator
- how those things relate (the rest)

## Wave Function
The wave function is quite simple. It is just a complex vector space. In Python, a 3D empty wave function could be:
```
n = 100
psi = np.zeros((n, n, n), dtype=complex)
```

The wave function serves as the state of our system. We will use the rest of Schrodinger's equation to determine how it should change in time, evolve a little bit by that description, and repeat. Because we can't fit an infinite space into our computer, we need to make a choice, in particular the shape of the wave function. Here I have decided the shape should be a cube with 100 elements along a side. When we want to map this vector space to a physical space, we'll need to pick a length for the edge of an element. We can't make a single decision about that, we'll decide when we know the physical situation we're describing. In fact, the same goes for the value of n, or that the shape is cubic.

Given that we are describing a finite space, and that Schrodinger's equation doesn't know that, we need to come up with a nice way to confine predictions to the space. We could decide that everything outside the space has infinite potential, but it's not clear how to actually implement that. Rather, let's say the result we're desiring from such an idea: the wave function should be confined to the finite space. So let's add a correction step in our evolution: normalize the wave function. This is basically saying "disregard any interactions with the space outside". At each step, we reset the state to exist exactly inside the finite space.

## Hamiltonian operator
We do not assume familiarity with Hamiltonian mechanics, so we'll explore enough to feel confident our eventual computation is true.

We'll bounce to classical mechanics, which is what Hamiltonian mechanics was made for. In classical mechanics, we need to choose a Hamiltonian (not an operator) for our system. A Hamiltonian can be figured from something called a Lagrangian, but Lagrangians are just siblings of Hamiltonians and offer no insights about how to pick them.

Rather, in the same way we guess that `F=ma` describes how a mass behaves when a force is applied, so too must we guess a Hamiltonian for any system we hope to analyze. However, we should be able to verify that our choice is correct by experiment. We are also lucky that people before us have guessed a bunch of Hamiltonians, and we can pick one from a list to try. For example, the Hamiltonian for a variety of systems is:
```
hamiltonian = kinetic_energy + potential_energy
```

While it would be interesting to see what we can do with this quantity, we should switch back to quantum mechanics first.

It is easy to imagine kinetic and potential energy as sums of individual particle positions and speeds, but in quantum mechanics we don't have particles. We have a wave function. So we need an operator to operate on the wave function to yield a meaningful potential.

For a single particle, the Hamiltonian operator should be:
```
# m: mass of particle
# h_bar: 6.62607015e-34 / (2 * math.pi)
def kinetic_energy(psi):
    return -(h_bar ** 2 / (2 * m)) * laplacian(psi)

def potential_energy(psi):
    v = np.zeros((n, n, n), dtype=float)  # we can choose any values, even vary with time, but the shape must match the wave function
    return v * psi

def hamiltonian(psi):
    return kinetic_energy(psi) + potential_energy(psi)
```

If the system behaves how we want it to, then we know we chose the correct Hamiltonian operator.

## The Rest
The remaining relation is quite simple. We need to calculate the time-derivative, so we'll do a small rearrangement.

```
def schrodinger(psi):
    return hamiltonian(psi) / (1j * h_bar)
```

# Avoiding Floating-point Limitations
In SI units, `h_bar` and `m` are very small. Yet we seek probabilities between 0 and 1. With floating-point computation, adding `1e-30` to `1` yields `1`. To avoid this, we look for a way for `h_bar` and `m` to be close to 1. `h_bar`'s dimension is `mass * length * length / time`. So if we decide to measure mass in `h_bar kg`, then `h_bar_compute` is `1` and compute masses are `mass_in_kg / h_bar`.
