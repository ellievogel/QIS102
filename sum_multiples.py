# sum_multiples.py

import numpy as np

"""
Display the sum of all natural numbers less than 1900 that are divisible by both 7 and 11
"""


def sum(n):
    # Generate vector for numbers through n, again assuming that we do not include 0
    natural_numbers = np.arange(1, n + 1)

    # Initialize sum variable
    return_sum = 0
    for index in range(n):
        # Declare number variable to make code easier to read
        number = natural_numbers[index]
        if number % 77 == 0:
            return_sum += number
    return return_sum


def main():
    n = 1900
    total = sum(n)
    # Print sum, with a comma for the thousands place
    print(f"Sum: {total:,}")


main()
