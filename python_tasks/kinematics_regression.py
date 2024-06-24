# kinematics_regression.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

"""
Takes in data from the data file kinematics_regression.csv
Calculates and displays the constant acceleration a and initial velocity v0 for a moving particle
Plots the (time, distance) values and draws a smooth curve through the values
"""


# Credit: Dr. Dave Biersach, from the course QIS102: Applied Quantum Computing
def fit_quadratic(x, y):
    # Reshape vector x to become matrix x
    x = x[:, np.newaxis]
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(x)
    # The matrix x2 will have two columns:
    # 1) the original x values and 2) the x**2 values
    x2 = np.array(transformer.transform(x))
    model = LinearRegression().fit(x2, y)
    initial_velocity = model.coef_[0]
    acceleration = 2 * model.coef_[1]
    a = model.coef_[1]
    b = model.coef_[0]
    c = model.intercept_
    return a, b, c, initial_velocity, acceleration


def main():
    # Open kinematics_regression.csv
    file_name = "kinematics_regression.csv"
    file_path = Path(__file__).parent / file_name
    data = np.genfromtxt(file_path, delimiter=",", skip_header=1)

    # Get time and distance data
    time = data[:, 0]
    distance = data[:, 1]

    # Plot points
    plt.figure(Path(__file__).name)
    plt.scatter(time, distance, color="red")

    # Calculate a, b, and c values for quadratic best fit curve, as well as the initial velocity and acceleration values
    a, b, c, initial_velocity, acceleration = fit_quadratic(time, distance)
    print(f"Initial velocity (v0): {initial_velocity:.4f} meters/second")
    print(f"Constant acceleration (a): {acceleration:.4f} meters/second^2")

    # Plot smooth curve through points
    plt.plot(time, a * time**2 + b * time + c, label="Quadratic", c="b")

    # Set axis labels, title, and show plot
    plt.title("Time vs. Distance for a particle")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Distance (meters)")
    plt.show()


main()
