# maxwell_bolzmann.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

"""
Show the Probability Density Function of the Maxwell-Boltzman distribution for the parameters a=1, a=2, and a=5
"""


# Helper function to produce the Maxwell-Boltzmann distribution, following the formula (sqrt(2/pi))(x^2 / a^3)(e^(-1x^2 / 2a^2))
def maxwell_bolzmann_dist(values, a):
    first_piece = np.sqrt(2 / np.pi)
    second_piece = np.power(values, 2) / np.power(a, 3)
    third_piece = np.exp((-1 * np.power(values, 2)) / (2 * np.power(a, 2)))
    return first_piece * second_piece * third_piece


def main():
    # Declare array of values, using 1000 steps to generate a continuous-looking function
    values = np.linspace(0, 20, 1000)
    # Find y values for the Maxwell-Boltzmann distribution, with parameters a = 1, 2, and 5
    y1 = maxwell_bolzmann_dist(values, 1)
    y2 = maxwell_bolzmann_dist(values, 2)
    y3 = maxwell_bolzmann_dist(values, 5)

    # Plot the 3 curves, setting the title and axis labels

    plt.figure(Path(__file__).name)
    plt.title("Maxwell-Boltzmann Distribution")
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Probability")
    plt.plot(values, y1)
    plt.plot(values, y2)
    plt.plot(values, y3)

    plt.show()


main()
