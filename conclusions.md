# Many electron orbital plots are misleading
In the wild, there are many plots of electron orbitals that show the real value of the wave function. Usually, the absolute real value of a 3D wave function is thresholded; positive values get one color and negative antoher. Surely there was a good reason to do this, but the plotting method is seen far more commonly than the explanation of why it is useful. Indeed, before I wrote this all, I had no idea I was sometimes seeing only the real value of a wave function, and I still don't know the reason for plotting this way.

# Computational complexity gets big fast
For an `n` dimensional cube cut into `e` pieces along each axis, with `m` particles, our computational complexity is `O(e ** (n * m))`. While there are certainly niches where optimizing can make an unreachable result reachable, this quantity grows so fast that a naive solution on a regular computer is likely similar to any other implementation. So for a single particle we can easily get away with a thousand or so space elements (1000 1D, 30x30 2D, 10x10x10 3D). For `m` particles, we can get away with `1000 ** (1/m)` space elements.

While I think the simulations done in this repo are pedagogically valuable, this computational complexity is likely why we don't see this approach used. Though it does seem pedagogical simulations are lagging computational improvements. Still, how many academic settings are there where big O notation and unintuitive physics are both present? It strikes me as normal that the physics and computing department are separate, but maybe it shouldn't be.

# Quantum mechanics is only mechanics
Like Newtonian mechanics, quantum mechanics can be used to describe a system of particles in space. The particles can interact in generic ways like repel smoothly or abruptly. But we only care about a potential energy, we cannot distinguish a potential caused by gravity or electric charge.

# Schrodinger equation is a wave equation; electron orbitals are standing waves; we cannot describe photons
First, a quick clarification. "The" wave equation relates the 2nd derivative over time to the 2nd derivative over space. But wave equations are equations solved by a wave, `f(x + v * t)`. If we let `u = x + v * t`,

```
"the" wave equation:
f''(u) = v ** 2 * f''(u)
we get an equation where we can solve for `u` -- that is, solved by a wave. Ideas that don't work have `x`s and `t`s hanging around.

Schrodinger equation (potential constant over time):
-i * h_bar * d[psi]/dt = -h_bar ** 2 / (2 * m) * laplace(psi) + v * psi
c1 * d[psi]/dt = c2 * laplace(psi) + c3 * psi
c1 * f'(u) = c2 * v ** 2 * f''(u) + c3 * f(u)
again we can solve for `u`.
```

Schrodinger equation is a wave equation. Electron orbitals are standing waves that show up when we look at the Coloumb potential of a nucleus. As such, with our current view, we cannot describe why an electron would ever decide to increase or decrease in energy. Any initial condition is the sum of some set of standing waves, and will oscillate forever (computations introduce error, which we've only managed enough to get a picture, not to see long-standing oscillations). A hydrogen spectrum comes from electrons that prefer one standing wave over another, but can discretely switch between them. Our electrons have no such preference.

# Quantum field theory is the next step
Maxwell's equations decribe electric and magnetic fields, and therefore photons. With a quantum description of fields, applied to electric and magnetic fields, we should be able to marry electrically charged quantum particles around a nucleus (electrons) with photons.

This was never clear to me. Quantum mechanics sounded like the whole thing, quantum electrodynamics and siblings sounded specific to the force they described, and quantum field theory sounded like a thin generic term for them. Quantum physics (which I took to be synonymous with quantum mechanics) seems to be the whole thing.

# This isn't about god's dice
While we do understand how the wave function relates to a probability, there's nothing random about these systems evolve. Obsession with observers and how they collapse wave functions seems to be rooted from something else in quantum physics.

# Quantum entanglement
While there isn't an example, we do have what we need to understand quantum entanglement. In the `collide_1d.py` example, two particles approach each other, repel, then move away from each other. Yet, we can imagine a wavefunction that is not a single blob. Say we have a two-particle wavefunction with one blob at `(a1, b1)` and another at `(a2, b2)`. If we observe a particle at `a1`, we know there's another at `b1`, and no one is at `a2` or `b2`.
