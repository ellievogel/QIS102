# agnesi_witch.py

import matplotlib.pyplot as plt
import numpy as np

"""
Shows Maria Agnesi's "witch" as a function of f(x) using the simplified equation where a = 1/2
Expresses f(x) as a power series over -1 < x < 1
Plots the exact value of f(x) and each version of its power series containing successively more terms from -1.5 < x < 1.5,
    starting with 2 terms and ending with 7 terms
Demonstrates that approximating a polynomial by adding successively more terms in its power series can be problematic
"""


# Simplified equation of formula utilizing a = 1/2: y = 1 / (x^2 + 1)
def f(x):
    return 1 / ((x**2) + 1)


# Helper function to return the power series for a given number of terms
# The power series of the derivative of arctan is (-1)^n * x^(2n)
def power_series(x, number_of_terms):
    series_sum = 0
    for n in range(number_of_terms):
        term = ((-1) ** n) * (x ** (2 * n))
        series_sum += term
    return series_sum


def main():
    # First, generate x-values and exact y-values and plot
    x_values = np.linspace(-1.5, 1.5, 1000)
    y_values = f(x_values)

    plt.plot(x_values, y_values, color="blue", label="Exact")

    # Initiate colormap so the plots can be generated in a loop with different colorings for clarity
    colormap = plt.cm.viridis
    # Iterate through power series representation from n=2 to n=7
    for term_number in range(2, 8):
        # Apply power_series to each value in x_values
        power_series_y_values = np.array(
            [power_series(x, term_number) for x in x_values]
        )
        plt.plot(
            x_values,
            power_series_y_values,
            color=colormap(term_number / 7),
            label=f"{term_number} terms",
        )

    # Provide title, axis labels, legend, and scale of axis
    plt.title("Runge's Phenomenon (Witch of Agnesi)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.ylim(-2, 2)
    plt.xlim(-1.75, 1.75)

    plt.show()


main()

"""
Comments on this function:
    Since the function is represented by y = 1 / (x^2 + 1) in its simplified form, expanding our evaluation into the complex demain has interesting implications.
    At +i and -i, the function f(z) has singularities where the denominator equals zero, and the presence of these singularities limits the power series' validity.
    Due to these singularities, the radius of convergence of the series is limited. This is why, as we approach x = -1 or x = 1, Agnesi's Witch diverges.
    Runge's Phenomenon occurs as the degree of an interpolating polynomial increases, oscillating significantly and leading to large errors.
    Agnesi's Witch demonstrates this phenomenon with its large oscillations near the endpoints.
"""
