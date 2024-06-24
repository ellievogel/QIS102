# plot3d_complex_sine.py

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator

"""
Uses matplotlib to draw the surface f(z) = |sin(z)| over the region +-2.5 +-i
"""

def f(z):
    return np.abs(np.sin(z))


def main():
    z_real = np.linspace(-2.5, 2.5, 1000)
    z_imag = np.linspace(-1, 1, 1000)

    z_real, z_imag = np.meshgrid(z_real, z_imag)
    z = z_real + 1j * z_imag
    f_z = f(z)

    plt.figure(Path(__file__).name)
    ax = plt.axes(projection="3d")

    surface = ax.plot_surface(z_real, z_imag, f_z, cmap="coolwarm", lw=0, antialiased=False)
    plt.colorbar(surface, ax=ax, shrink=0.5)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter("{x:.02f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.show()

main()

    