# lcm_gcd.py

import math

"""
Calculate the lowest common multiple (LCM) of two integers using only basic arithmetic operators and Python's built-in GCD function
"""

# The least common denominator can be found by multiplying the two numbers together, and then dividing it by the greatest common denominator.


def lcm(a, b):
    # Multiply numbers together
    multiplied_value = a * b
    # Calculate GCD
    greatest_common_denominator = math.gcd(a, b)
    return_value = multiplied_value // greatest_common_denominator
    return return_value


def main():
    least_common_multiple = lcm(447618, 2011835)
    print(f"The LCM of 447618 and 2011835 is {least_common_multiple}")


main()
