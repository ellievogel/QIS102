# hamming_weight.py

import numpy as np

"""
Calculate the Hamming Weight of a base 10 integer
"""


def convert_to_binary(number):
    # Utilize the binary representation function in numpy to convert integer number to string of 0s and 1s
    str = np.binary_repr(number, width=None)
    return str


def main():
    number = 95601
    binary_representation = convert_to_binary(number)
    # Utilize the count function to count how many times a 1 appears in the binary representation
    count_of_ones = binary_representation.count("1")
    print(f"The Hamming weight of {number:,} is {count_of_ones}.")


main()
