# werner_formula.py

import matplotlib.pyplot as plt
import numpy as np

"""
Graphs f1(x) = sin(0.8x), f2(x) = sin(0.5x), f3(x) = f1 * f2, and f4 = Werner's Product-to-sum formula for f1 * f2
Uses the domain -3*pi <= x <= 3*pi subdivided into 100 intervals
"""


# Helper function for f1
def f1(x):
    return np.sin(0.8 * x)


# Helper function for f2
def f2(x):
    return np.sin(0.5 * x)


# Helper function for f3
def f3(x):
    return f1(x) * f2(x)


# Werner's formula for sin(a)sin(b) = cos(a - b) - cos(a + b)
def f4(x):
    return (np.cos(0) - np.cos(2 * x)) / 2


def main():
    # Generate x-values and plot each of the functions on the given interval
    x_values = np.linspace(-3 * np.pi, 3 * np.pi, 100)
    plt.plot(x_values, f1(x_values), label=r"$f_1(x) = \sin(0.8x)$", color="red")
    plt.plot(x_values, f2(x_values), label=r"$f_2(x) = \sin(0.5x)$", color="blue")
    plt.plot(
        x_values, f3(x_values), label=r"$f_3(x) = f_1(x) \cdot f_2(x)$", color="green"
    )
    plt.scatter(
        x_values,
        f4(x_values),
        marker="o",
        facecolors="none",
        edgecolors="grey",
        label=r"$f_4(x) = \text{Werner\'s Product-to-sum formula}$",
    )

    # Set plot title, axis labels, and legend
    plt.title("f1(x), f2(x), f3(x), and f4(x)")
    plt.xlabel("x")
    plt.ylabel("y")

    # Set x-axis to range from -3*pi to 3*pi, with appropriate labels
    ticks = np.arange(-3 * np.pi, 3 * np.pi + 1, np.pi)
    tick_labels = []
    for tick in ticks:
        if tick == 0:
            tick_labels.append("0")
        else:
            tick_labels.append(f"{tick/np.pi:.0f}$\pi$")

    plt.xticks(ticks, tick_labels)
    plt.legend()

    plt.show()


main()
