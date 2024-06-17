# eulers_constant.py

"""
Utilize SciPy to numerically estimate Euler's Constant
Superimpose a line graph of Euler's Constant + ln(x) on top of a step plot of the first 50 Harmonic Numbers
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


# Helper function to produce an array of the first 50 Harmonic Numbers
def harmonic_numbers(n):
    numbers = np.zeros(n)
    numbers[0] = 1
    for index in range(1, n):
        numbers[index] = numbers[index - 1] + (1 / (index + 1))
    return numbers


# Define function to be integrated to produce Euler's Constant
def integrand(x):
    return -1 * np.log(np.log(1 / x))


def main():
    # Gamma represents Euler's constant
    gamma = quad(integrand, 0, 1, full_output=True, limit=1000)[0]

    # Plot line graph of y = gamma + ln(x)
    plt.figure()
    x_coordinates_line_graph = np.linspace(1, 50, 1000)
    y_coordinates_line_graph = gamma + np.log(x_coordinates_line_graph)

    plt.plot(x_coordinates_line_graph, y_coordinates_line_graph)

    # Plot step plot of first 50 harmonic numbers
    x_coordinates = np.arange(1, 51, 1)
    harmonic = harmonic_numbers(50)
    plt.step(x_coordinates, harmonic)

    # Set title and axis labels
    plt.title(
        r"Step plot of first 50 Harmonic numbers and superimposed line graph of the function $y = gamma + ln(x)$"
    )
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


main()
