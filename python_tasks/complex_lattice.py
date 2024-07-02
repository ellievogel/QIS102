from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

"""
Renders a scatter plot using an equal aspect ratio of the complex function: f(z) = z^2 + iz + 1, |Re(z)| <= 4, 0 <= Im(z) <= 2
Generates the number of Gaussian Integers given f(z) when the absolute value of both the real and imaginary components are less than or equal to 10
"""

def generate_plot(real_range, imaginary_range):
    # Generate arrays of allowed real and imaginary component values, with a step of 1000 to appear continuous
    real_values = np.linspace(*real_range, 1000)
    imaginary_values = np.linspace(*imaginary_range, 1000)
    
    # Create a grid of complex numbers
    real_grid, imaginary_grid = np.meshgrid(real_values, imaginary_values)
    z = real_grid + 1j * imaginary_grid
    
    # Compute the function f(z) = z^2 + iz + 1
    f_z = z**2 + 1j * z + 1
    
    # Plot the real and imaginary parts of f(z)
    plt.figure(Path(__file__).name)
    plt.scatter(f_z.real, f_z.imag, c=f_z.real, cmap="Blues")
    plt.scatter(gaussian_int_real, gaussian_int_imag, color='red')

    plt.title(r"$f(z) = z^2 + iz + 1$")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.axis("equal")
    plt.show()

def main():
    # Create arrays of integers for real and imaginary parts
    real_integers = np.arange(-5000, 5001)
    imaginary_integers = np.arange(-5000, 5001)
    
    # Create global variables to store the real and imaginary components of Gaussian Integers for plotting later
    global gaussian_int_real
    global gaussian_int_imag
    gaussian_int_real = []
    gaussian_int_imag = []
    
    # Use meshgrid to create a grid of integers
    real_grid, imaginary_grid = np.meshgrid(real_integers, imaginary_integers)
    z = real_grid + 1j * imaginary_grid
    
    # Compute the function f(z) = z^2 + iz + 1
    f_z = z**2 + 1j * z + 1
    
    # Find Gaussian Integers where both the real and imaginary parts are within the specified bounds
    mask = (np.abs(f_z.real) <= 10) & (np.abs(f_z.imag) <= 10)
    gaussian_int_real = real_grid[mask]
    gaussian_int_imag = imaginary_grid[mask]
    gaussian_integers = np.sum(mask)
    
    print(f"There are {gaussian_integers} Gaussian Integers where |Re(f(z))| <= 10 and |Im(f(z))| <= 10")
    
    # Set allowed values for real and imaginary components
    real_range = (-4, 4)
    imaginary_range = (0, 2)
    generate_plot(real_range, imaginary_range)

main()