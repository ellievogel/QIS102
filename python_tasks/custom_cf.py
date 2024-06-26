# custom_cf.py

import numpy as np

"""
Python program to display the standard continued fraction for 9 real numbers determined by x_n = (1 + sqrt(4n^2 - 4n + 5)) / 2
"""


def normalize_cf(cf):
    # Simplify the representation of a given continued fraction
    while len(cf) > 2 and cf[-1] == 1 and cf[-2] != 1:
        cf[int(-2)] += 1
        cf.pop(-1)
    return cf


def encode_cf(x):
    # Change number into its continued fraction representation
    cf: list[int] = []
    MAX_TERMS = 7  # Set to display only 7 terms of each continued fraction
    while len(cf) < MAX_TERMS:
        cf.append(int(x))
        x = x - int(x)
        if x < 1e-11:
            break
        x = 1 / x
    return normalize_cf(cf)


def decode_cf(cf):
    # Standard technique to change continued fraction into its decimal representation
    h_n, k_n = 0, 0
    b_1, h_1, k_1 = 1, 1, 0
    h_2, k_2 = 0, 1
    for term in cf:
        a_n, b_n = term, 1
        h_n = a_n * h_1 + b_1 * h_2
        k_n = a_n * k_1 + b_1 * k_2
        b_1 = b_n
        h_1, h_2 = h_n, h_1
        k_1, k_2 = k_n, k_1
    return h_n / k_n


def eval_cf(x):
    # Encode the continued fraction, then decode, printing out each value to show the relativity of the approximation
    cf = encode_cf(x)
    x2 = decode_cf(cf)
    print(f"{x} -> {cf} -> {x2}")


def main():
    n = 9  # Set the number of terms you are looking for
    integers = np.arange(1, n + 1)

    # Use numpy's sqrt function to construct an array of the numbers we will apply the continued fraction functions to
    numbers = (1 + np.sqrt(4 * (integers**2) - 4 * integers + 5)) / 2

    for number in numbers:
        eval_cf(number)


main()
