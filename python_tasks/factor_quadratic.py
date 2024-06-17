# factor_quadratic.py

import numpy as np

"""
Factor quadratic Jx^2 + Kx + L, factoring out the greatest common denominator and identifying/deleting any duplicate factorizations
"""


def main():
    J = 115425
    K = 3254121
    L = 379020

    print("Given the quadratic:")
    print(f"{J}x^2 + {K}x + {L} = 0")
    print("The factors are:")

    found_factor = False

    factor_set = set()

    greatest_common_denominator = np.gcd(
        J, np.gcd(K, L)
    )  # Find greatest common denominator of the polynomial

    J = J // greatest_common_denominator  # Adjust the numbers before factoring
    K = K // greatest_common_denominator
    L = L // greatest_common_denominator

    for a in range(1, J + 1):
        if J % a == 0:
            c = J // a
            for b in range(1, L + 1):
                if L % b == 0:
                    d = L // b
                    if a * d + b * c == K:
                        if (
                            (c, d) in factor_set
                        ):  # Check if this set of factors has already been found
                            continue
                        else:
                            if greatest_common_denominator != 1:
                                print(f"{greatest_common_denominator}", end="")
                            print(f"({a}x + {b})({c}x + {d})")
                            factor_set.add((a, b))
                        found_factor = True

    if not found_factor:
        print("There are no factors.")
        print("The quadratic is prime.")


main()
