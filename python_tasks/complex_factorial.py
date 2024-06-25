# complex_factorial.py

import numpy as np
from scipy.integrate import quad

"""
Computes the value of i!
Utilizes:
    Euler's formula in complex analysis: e^{ix} = cos(x) + i\sin(x)
    SciPy integrate for the gamma function, as described at https://en.wikipedia.org/wiki/Gamma_function
    Indefinite integrals over the real and imaginary components
"""


# Helper function to integrate the real part of the indefinite integral
def integrand_real(t, z):
    # Original formula: (t ** (z - 1)) * exp(-t)
    # Utilizes Euler's formula to extract real component only
    # Help debugging conversion: ChatGPT
    return (t ** (z.real - 1)) * np.exp(-t) * np.cos(z.imag * np.log(t))


# Helper function to integrate the imaginary part of the indefinite integral
def integrand_imag(t, z):
    # Original formula: (t ** (z - 1)) * exp(-t)
    # Utilizes Euler's formula to extract imaginary component only
    # Help debugging conversion: ChatGPT
    return (t ** (z.real - 1)) * np.exp(-t) * np.sin(z.imag * np.log(t))


# Gamma function utilizing both indefinite integrals
def gamma(z):
    real_part = quad(integrand_real, 0, np.inf, args=(z))[0]
    imag_part = quad(integrand_imag, 0, np.inf, args=(z))[0]
    return real_part + 1j * imag_part


def main():
    # Compute i!, using the formula n! = gamma(n+1)
    z = 1j
    i_factorial = gamma(z + 1)
    print(f"i! is equal to {i_factorial:.6f}")


main()
