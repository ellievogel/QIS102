# benfords_law.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from mpmath import mpf, power

"""
Demonstrate the Law of Anomalous Numbers by calculating the probability of each digit appearing as the most significant digit in 100,000 very large random integers
"""


# Helper function to raise each number to the 100th power and return the most significant digit
def raise_and_most_significant_digit(number):
    # Convert the number to an mpf object since the number will be large
    number = mpf(str(number))
    # Raise the number to the 100th power
    raised_number = power(number, 100)
    # Convert back to a string for indexing
    string_number = str(raised_number)
    # Return the first index of the string, or the most significant digit, casting it as an integer
    return int(string_number[0])


def main():
    # Initialize array to hold the counts of each digit using np.zeros
    counts = np.zeros(9)

    # Initialize large numbers
    number_set = np.random.randint(1, 1000001, size=100000)

    # Call helper function to raise each number to the 100th power and determine the leading digit for each number
    for number in number_set:
        leading_digit = raise_and_most_significant_digit(number)
        # Increment proper index in counts by 1
        counts[leading_digit - 1] += 1

    # Convert counts to probabilities
    probabilities = counts / len(number_set)

    # Plot data, setting the title and axis labels of the graph
    plt.figure(Path(__file__).name)
    plt.bar(np.arange(1, 10), probabilities)

    plt.tick_params("x")
    plt.title("Digit Probabilities According to Benford's Law")
    plt.xlabel("Digit")
    plt.ylabel("Probability")
    plt.show()


main()
