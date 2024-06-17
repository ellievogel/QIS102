# archimedes_spiral.py

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

"""
Calculates and displays the arc length of an Archimedes Spiral with r = theta as it rotates from 0 <= theta <= 8*pi
Graphs the spiral
"""


# Calculate arc length of spiral utilizing equation for arc length of Archimedes Spiral, s(theta) = integral from 0 to 8*pi of (sqrt(theta^2 + 1)) d(theta)
def integrand(theta):
    return np.sqrt(theta**2 + 1)


def calculate_arc_length(theta):
    arc_length = quad(integrand, 0, 8 * np.pi, full_output=True, limit=1000)[0]
    return arc_length


def plot_spiral(range):
    r = np.linspace(0, range, 1000)  # Have theta run from 0 to 8 * pi, with 1000 steps

    # Calculate x and y coordinates, knowing that theta = r
    x_coordinates = r * np.cos(r)
    y_coordinates = r * np.sin(r)

    # Plot graph
    plt.figure()
    plt.plot(x_coordinates, y_coordinates)

    # Set title and axis labels
    plt.title(r"Archimedes Spiral with $\theta$ ranging from $0$ to $8\pi$")
    plt.xlabel("x")
    plt.ylabel("y")

    # Create tick marks
    ticks = np.arange(-8 * np.pi, 9 * np.pi, np.pi)
    tick_labels = []
    for tick in ticks:
        if tick == 0:
            tick_labels.append('0')
        else:
            tick_labels.append(f'{tick/np.pi:.0f}$\pi$')

    plt.xticks(ticks, tick_labels)
    plt.yticks(ticks, tick_labels)

    plt.axhline(0, color="black", linewidth=2)
    plt.axvline(0, color="black", linewidth=2)

    plt.grid("on")
    plt.gca().set_aspect("equal")
    plt.show()


def main():
    range = 8 * np.pi
    arc_length = calculate_arc_length(range)
    print(f"Arc Length: {arc_length:.10f}")
    plot_spiral(range)


main()
