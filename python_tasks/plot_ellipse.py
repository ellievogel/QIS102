# plot_ellipse.py

import matplotlib.pyplot as plt
import numpy as np

"""
Displays a full 2D graph of an ellipse with a major axis of length 100 on the x-axis and a minor axis of length 50 on the y-axis, centered at the origin.
The polar equation for an ellipse centered at the origin is r = sqrt((a^2*b^2) / (b^2cos^2(theta) + a^2sin^2(theta)))
"""


def main():
    theta = np.linspace(
        0, 2 * np.pi, 1000
    )  # Have theta run from 0 to 2 * pi, with 1000 steps

    a = 100
    b = 50

    numerator = (a**2) * (b**2)
    denominator = (b**2) * ((np.cos(theta)) ** 2) + (a**2) * ((np.sin(theta)) ** 2)

    radius = np.sqrt(numerator / denominator)

    # Translate polar coordinates into cartesian ones for plotting
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Plot graph
    plt.figure()
    plt.plot(x, y)

    # Set title and axis labels
    plt.title(r"$\frac{x^2}{100^2} + \frac{y^2}{50^2} = 1$")
    plt.xlabel("x")
    plt.ylabel("y")

    # Change tick marks and make major axis bold
    plt.yticks(np.arange(-b, b + 10, 10))
    plt.xticks(np.arange(-a, a + 20, 20))
    plt.axhline(0, color="black", linewidth=2)
    plt.axvline(0, color="black", linewidth=2)

    plt.grid("on")
    plt.gca().set_aspect("equal")
    plt.show()


main()
