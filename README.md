Apply Schrodinger's equation to a wave function repeatedly to see it evolve as a dynamic system.

We are not interested to simplify in traditional ways. We are not here to avoid math that can't be tested on an exam, complex computations, visualizations, or unintuitive physical concepts. We will see what is truly going on first, and _then_ make intuitions and justify assumptions and simplifications from there.

We reject the notion that "nobody understands quantum mechanics" and instead suppose that the pedagogy around quantum mechanics is underdeveloped. And start to fill that void.

Suggested order:
- read `theory.md` and `schrodinger.py`
- (run `pip install -r requirements.txt`)
- run & read `./run_example.py examples/well_1d.py`
- run & read `./run_example.py examples/packet_1d.py`
- run & read `./run_example.py examples/packet_2d.py`
- run & read `./run_example.py examples/double_slit.py`
- run & read `./run_example.py examples/packet_3d.py`
- read `constants.py`, `potential.py`, and `initial.py`
- run & read `./run_example.py examples/orbital_1d.py`
- run & read `./run_example.py examples/orbital.py`
    - run `n=2 ./run_example.py examples/orbital.py`
    - run `n=2 l=1 m=0 ./run_example.py examples/orbital.py`
    - run `axis=x n=2 l=1 m=0 ./run_example.py examples/orbital.py`
    - run `tomograph=1 n=2 l=1 m=0 ./run_example.py examples/orbital.py`
    - run `n=2 l=1 m=1 ./run_example.py examples/orbital.py`
    - run `axis=x n=2 l=1 m=1 ./run_example.py examples/orbital.py`
    - run `tomograph=1 n=2 l=1 m=1 ./run_example.py examples/orbital.py`
    - run `tomograph=1 axis=x n=2 l=1 m=1 ./run_example.py examples/orbital.py`
- run & read `./run_example.py examples/collide_1d.py`

This project assumes familiarity with:
- Python
- numpy
- vector calculus
- complex numbers

Inspired by [this video](https://www.youtube.com/watch?v=MXs_vkc8hpY).
