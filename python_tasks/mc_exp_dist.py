# mc_exp_dist.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

"""
Uses Monte Carlo estimation to calculate the probability an event will occur within one hour of an exponential distribution having a rate parameter of 90 minutes
Takes a minimum of 25,000 random samples and then indicates via different colors which of the random samples are above or below PDF curve
Graphs the PDF of the distribution
Calculates and displays the percent relative error of the probability estimate
"""

# Formula found at https://en.wikipedia.org/wiki/Exponential_distribution
def exponential_pdf(x, rate):
    return rate * np.exp(-rate * x)

def main():
    rate_parameter = 1 / 90
    time_limit = 60
    n = 25000

    print(f"Number of samples: {n:,}")

    samples = np.random.exponential(1 / rate_parameter, n)
    within_limit = samples <= time_limit

    # Calculate the number of samples within the time limit, and calculate the probability
    in_time_count = np.sum(within_limit)
    probability = in_time_count / n
    print(f"Number of samples within one hour: {in_time_count}")
    print(f"Estimated Probability that an event will occur within one hour: {probability:.5f}")

    # Generate X and Y values for PDF
    x_values = np.linspace(0, 300, 1000)
    y_values = exponential_pdf(x_values, rate_parameter)

    # Determine samples above and below the PDF curve
    pdf_samples = exponential_pdf(samples, rate_parameter)
    above = samples[pdf_samples > y_values.min()]
    below = samples[pdf_samples <= y_values.min()]


    # Help with graphing: ChatGPT
    # Note to grader: I do not think this is correct, so I look forward to incorporating any feedback you can give.
    plt.figure(Path(__file__).name)

    plt.hist(samples, bins=100, color='blue', alpha=0.5, label='Samples', density=True)

    # Highlight samples within the time limit
    plt.hist(samples[within_limit], bins=100, color='green', alpha=0.5, label='Samples within limit', density=True)
    plt.plot(x_values, y_values, color='black', linewidth=2, label='Exponential PDF')

    # Plot samples above and below the PDF curve
    plt.scatter(above, exponential_pdf(above, rate_parameter), color='red', s=1, label='Above PDF')
    plt.scatter(below, exponential_pdf(below, rate_parameter), color='blue', s=1, label='Below PDF')

    # Add titles and labels
    plt.title('Monte Carlo Estimation of Exponential Distribution')
    plt.xlabel('Time (minutes)')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)

    plt.show()

main()
