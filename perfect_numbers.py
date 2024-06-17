# perfect_numbers.py

import numpy as np

"""
Print out each perfect number from 2 to 10,000, and print out the sum of the reciprocals of its divisors
"""


def is_perfect(n):
    x = np.arange(1, n)
    factors = x[np.where(n % x == 0)]
    return np.sum(factors) == n


# Given a perfect number n, what is the sum of the reciprocals of its divisors (including 1 and n?)


def sum_of_reciprocals(n):
    x = np.arange(1, n + 1)  # Create the same array, but include n this time
    factors = x[
        np.where(n % x == 0)
    ]  # Same process as before to create array of factors
    reciprocals = 1 / factors  # Create the reciprocals of the factors
    return np.sum(reciprocals)  # Return the sum


def main():
    for n in range(2, 10_000):
        if is_perfect(n):
            reciprocal_sum = sum_of_reciprocals(n)

            # Calculate the sum of the reciprocals of n's divisors
            print(f"{n:,} is a perfect number")
            print(
                f"The sum of the reciprocals of its divisors for {n:,} is {reciprocal_sum:.2}"
            )


main()
