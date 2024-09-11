import math

planck_length = 1.616255e-35
planck_mass = 2.176434e-8
planck_time = 5.391247e-44
planck_charge = 1.875546e-18

h_bar = 6.62607015e-34 / (2 * math.pi)  # reduced Planck constant, kg m2 / s
h_bar_planck = 1
h_bar_compute = h_bar_planck
assert abs(h_bar_compute - h_bar / planck_mass / planck_length ** 2 * planck_time) < 1e-3

epsilon_0 = 8.85418782e-12  # vacuum permittivity, s4 A2 / kg m3
epsilon_0_planck = epsilon_0 / planck_time ** 2 / planck_charge ** 2 * planck_mass * planck_length ** 3
epsilon_0_compute = epsilon_0_planck
e = 1.602176634e-19  # electron charge, C
e_planck = e / planck_charge
e_compute = e_planck
assert abs(math.log10(e_compute ** 2 / epsilon_0_compute ** 2)) < 2

m_e = 9.1093837139e-31  # mass of electron, kg
m_e_planck = m_e / planck_mass
m_e_compute = 1  # we simply decide that electrons have mass of 1 in our simluated universe

c = 299792458  # speed of light, m / s
c_planck = 1
c_compute = c_planck
assert abs(c_compute - c / planck_length * planck_time) < 1e-3

alpha = 0.0072973525643  # fine-structure constant, unitless

a_0 = h_bar / (m_e * c * alpha)  # bohr radius, m
a_0_compute = h_bar_compute / (m_e_compute * c_compute * alpha)
assert a_0_compute - 4 * math.pi * epsilon_0_compute * h_bar_compute ** 2 / (e_compute ** 2 * m_e_compute) < 1e-3
