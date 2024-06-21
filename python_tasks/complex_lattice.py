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

    # Generate arrays to store values for plotting on imaginary plane
    reals = []
    imaginary = []

    # Iterate through each coordinate defined by a real and imaginary component pair
    for real_value in real_values:
        for imaginary_value in imaginary_values:
            real_part = real_value**2 - imaginary_value**2 - imaginary_value + 1
            imaginary_part = 2 * real_value * imaginary_value + real_value
            # Append real and imaginary parts for plotting of the point
            reals.append(real_part)
            imaginary.append(imaginary_part)

    # Generate scatter plot of complex function, setting aspect ratio to equal
    plt.figure(Path(__file__).name)
    plt.scatter(reals, imaginary, c=reals, cmap="Blues")
    plt.scatter(gaussian_int_real, gaussian_int_imag)

    plt.title(r"$f(z) = z^2 + iz + 1$")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.axis("equal")
    plt.show()


def main():
    # Create arrays of integers for real and imaginary parts
    real_integers = np.arange(-500, 501)
    imaginary_integers = np.arange(-500, 501)
    # Store number of Gaussian Integers
    gaussian_integers = 0
    # Create global variables to store the real and imaginary components of Gaussian Integers for plotting later
    global gaussian_int_real
    gaussian_int_real = []
    global gaussian_int_imag
    gaussian_int_imag = []

    # Determine Gaussian Integers
    for i in real_integers:
        for j in imaginary_integers:
            real_part = i**2 - j**2 - j + 1
            imaginary_part = 2 * i * j + i
            if abs(real_part) <= 10 and abs(imaginary_part) <= 10:
                gaussian_integers += 1
                gaussian_int_real.append(i)
                gaussian_int_imag.append(j)

    print(
        f"There are {gaussian_integers} Gaussian Integers where |Re(f(z))| <= 10 and |Im(f(z))| <= 10"
    )

    # Set allowed values for real and imaginary components
    real_range = (-4, 4)
    imaginary_range = (0, 2)
    generate_plot(real_range, imaginary_range)


main()
