# mc_exp_dist.py

from pathlib import Path

import matplotlib.pyplot as plt
import numba
import numpy as np
from numba import float64, vectorize

"""
Uses Monte Carlo estimation to calculate the probability an event will occur within one hour of an exponential distribution having a rate parameter of 90 minutes.
Takes a minimum of 25,000 random samples and then indicates via different colors which of the random samples are above or below the PDF curve.
Graphs the PDF of the distribution.
Calculates and displays the percent relative error of the probability estimate.
"""


# Formula found at https://en.wikipedia.org/wiki/Exponential_distribution
@vectorize([float64(float64, float64)], nopython=True)
def exponential_pdf(x: float, rate: float):
    return rate * np.exp(-rate * x) if x >= 0 else 0


# Helper function to generate random numbers using the Halton method
@vectorize([float64(float64, float64)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h


# Helper function to calculate the exact value
@vectorize([float64(float64, float64)], nopython=True)
def exp_exact(time_limit, rate_parameter):
    1 - np.exp(-rate_parameter * time_limit) if time_limit >= 0 else 0


def main():
    rate_parameter = 1 / 90
    time_limit = 60

    n = 25_000

    print(f"Number of samples: {n:,}")

    # Generate random samples
    samples_x = (1 - halton(np.arange(n), 2)) * time_limit
    samples_y = (1 - halton(np.arange(n), 3)) * rate_parameter * 1.5

    d = samples_y - exponential_pdf(samples_x, rate_parameter)

    # Check which samples fall within the one hour range and sort them accordingly
    samples_in_x = samples_x[d <= 0.0]
    samples_in_y = samples_y[d <= 0.0]
    samples_out_x = samples_x[d > 0.0]
    samples_out_y = samples_y[d > 0.0]

    # Calculate the actual and estimated probabilities, as well as the percent error
    actual = exp_exact(time_limit, rate_parameter)
    estimated = np.count_nonzero(d <= 0.0) / n
    error = np.abs((estimated - actual) / actual)

    # Calculate the number of samples within the time limit, and calculate the probability
    print(
        f"Estimated Probability that an event will occur within one hour: {estimated:.5f}"
    )
    print(f"Percent Relative Error: {error:.2f}%")

    # Generate X and Y values for PDF
    x = np.linspace(0, 100, 1000)
    y = exponential_pdf(x, rate_parameter)

    plt.figure(Path(__file__).name)
    plt.plot(x, y, label="Exponential PDF")

    plt.scatter(samples_in_x, samples_in_y, color="blue")
    plt.scatter(samples_out_x, samples_out_y, color="red")

    # Add titles and labels
    plt.title("Monte Carlo Estimation of Exponential Distribution")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.grid(True)

    plt.show()


main()
