# iris_analysis.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

"""
Visualizes plant data downloaded from https://archive.ics.uci.edu/dataset/53/iris
Generates a scatter plot of the three different flower types, graphing petal length vs. petal width
"""


# Helper function to plot each set of points
def plot_points(array, color, label):
    lengths = []
    widths = []
    for tuple in array:
        lengths.append(tuple[0])
        widths.append(tuple[1])
    # Create specific plot with specified color and label for legend
    plt.scatter(lengths, widths, color=color, label=label)


def main():
    # Open iris.names
    file_name = "iris.data"
    file_path = Path(__file__).parent / file_name
    # Specifying data types to avoid nan data error (source for this line: ChatGPT)
    data = np.genfromtxt(
        file_path,
        delimiter=",",
        dtype=[("f0", "f8"), ("f1", "f8"), ("f2", "f8"), ("f3", "f8"), ("f4", "U20")],
    )

    # Get flower data
    petal_length = data["f2"]
    petal_width = data["f3"]
    names = data["f4"]

    # Create arrays to separate out types of flowers
    setosa = []
    versicolor = []
    virginica = []

    for index in range(0, petal_length.size):
        # Separate data
        if names[index] == "Iris-setosa":
            setosa.append((petal_length[index], petal_width[index]))
        elif names[index] == "Iris-versicolor":
            versicolor.append((petal_length[index], petal_width[index]))
        elif names[index] == "Iris-virginica":
            virginica.append((petal_length[index], petal_width[index]))

    plt.figure(Path(__file__).name)

    # Call helper function to plot each flower variety with varying colors and labels
    plot_points(setosa, "b", "Iris-setosa")
    plot_points(versicolor, "r", "Iris-versicolor")
    plot_points(virginica, "g", "Iris-virginica")

    # Set axis labels, title, and show plot
    plt.title(
        "Petal lengths and widths for Iris-setosa, Iris-versicolor, and Iris-virginica"
    )
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal width (cm)")
    plt.legend()
    plt.show()


main()
