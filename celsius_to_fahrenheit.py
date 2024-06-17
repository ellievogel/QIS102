# celsius_to_farenheit.py

import numpy as np

"""
Generate Celsius-Farenheit pairs for each temperature ranging from -44 to 104 increasing by 4
"""


def main():
    # Generate a vector of the celsius numbers starting at -44 and going up to 104 (inclusive) with a step of 4
    celsius_numbers = np.arange(-44, 105, 4)

    # Perform the conversion on the celsius_numbers vector
    farenheit_numbers = (celsius_numbers * (9 / 5)) + 32

    for index in range(0, np.size(celsius_numbers) - 1):
        # Obtain the celsius and farenheit values for a particular pair
        celsius = celsius_numbers[index]
        farenheit = farenheit_numbers[index]
        # Print the value pairs, using 6 digits to the left of the decimal to create a more clean print, and using 2 digits to the right of the decimal as specified in the prompt.
        print(f"C: {celsius:>6.2f}, F: {farenheit:>6.2f}")


main()
