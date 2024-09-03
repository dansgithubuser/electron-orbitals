# Schrodinger's Equation
Schrodiner's equation comes in a few forms. We're interested in the "time-dependent" form, which is the general form. We'll split this equation into three parts:
- a wave function
- a Hamiltonian
- how those things relate (the rest)

## Wave Function
The wave function is quite simple. It is just a complex vector space. In Python, a 3D empty wave function could be:
```
n = 100
psi = np.zeros((n, n, n), dtype=complex)
```

The wave function serves as the state of our system. We will use the rest of Schrodinger's equation to determine how it should change in time, evolve a little bit by that description, and repeat. Because we can't fit an infinite space into our computer, we need to make a choice, in particular the shape of the wave function. Here I have decided the shape should be a cube with 100 elements along a side. When we want to map this vector space to a physical space, we'll need to pick a length for the edge of an element. We can't make a single decision about that, we'll decide when we know the physical situation we're describing. In fact, the same goes for the value of n, or that the shape is cubic.

Given that we are describing a finite space, and that Schrodinger's equation doesn't know that, we need to come up with a nice way to confine predictions to the space. We could decide that everything outside the space has infinite potential, but it's not clear how to actually implement that. Rather, let's say the result we're desiring from such an idea: the wave function should be confined to the finite space. So let's add a correction step in our evolution: normalize the wave function. This is basically saying "disregard any interactions with the space outside". At each step, we reset the state to exist exactly inside the finite space.

## Hamiltonian


## The Rest
The remaining relation is quite simple. We need to calculate the time-derivative, so we'll do a small rearrangement.

```
h_bar = 6.62607015e-34 / (2 * math.pi)
dpsi = hamiltonian(psi) / (1j * h_bar)
```
