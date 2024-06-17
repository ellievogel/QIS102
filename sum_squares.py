# sum_squares.py

import numpy as np

"""
Display the sum of the first 1,000 natural numbers squared, checking with Gaussian summation
"""


def main():
    # Assuming we are not including 0 as a natural number, create vector going up to 1000 (inclusive)
    natural_numbers = np.arange(1, 1001)

    # Square the numbers
    squared_numbers = (natural_numbers) ** 2

    # Generate a sum
    sum = np.sum(squared_numbers)

    # Utilize Gaussian summation to generate the sum
    gaussian_sum = ((2 * (1000**3)) + (3 * (1000**2)) + 1000) / 6

    print(f"Sum from code: {sum:,}")
    print(f"Gaussian sum: {gaussian_sum:,.0f}")


main()
