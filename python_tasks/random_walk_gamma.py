# random_walk_gamma.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

"""
Plot the expected distance of a uniform random walk of N steps on a unit lattice having dimension d for 1 <= d <= 25 and n = 20000
"""


# Helper function to calculate the distance given the formula
def distance(N, d):
    first_term = np.sqrt((2 * N) / d)
    second_term_numerator = gamma(d + 1) / 2
    second_term_denominator = gamma(d / 2)
    return first_term * ((second_term_numerator / second_term_denominator) ** 2)


def main():
    d = 25  # Set values of d and N in a way that makes them easy to change in the future
    N = 20_000
    d_values = np.linspace(
        1, d, 1000
    )  # Create an array of values for d, setting the number of steps to 1000 to generate a more continuous curve
    distance_values = distance(
        N, d_values
    )  # Calculate the distance values for each point in the d_values array

    # Set plot settings, add axis labels, and show plot
    plt.figure(Path(__file__).name)
    plt.plot(d_values, distance_values)
    plt.title(
        "Distance of a uniform random walk on a unit lattice at different dimensions"
    )
    plt.xlabel("Dimension")
    plt.ylabel("Estimated Distance")
    plt.grid("on")
    plt.show()


main()
