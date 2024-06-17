# lead_attenuation.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

"""
Uses SciPy to compute and plot the estimated attenuation factor of a lead shield as a function of incident photon energy.
Takes in input from lead_attenuation.csv, which contains data for different photons' energies and the lead shield's attenuation factor for that energy.
Displays the data on a semi-log scale on the y-axis, utilizing a cubic spline interpolation to draw a smooth curve through the points.
Calculates the attenuation coefficient for a photon with 4.65 MeV energy.
Calculates the percent of photons passing through a lead shield that is 2 cm thick.
"""


# Helper function to determine the percent of photons passing through a lead shield 2 cm thick
def percent(attenuation):
    return np.exp(-2 * attenuation)


def main():
    file_name = "lead_attenuation.csv"
    file_path = Path(__file__).parent / file_name

    # Produce points for scatter plot from .csv file
    samples = np.genfromtxt(file_path, delimiter=",", skip_header=1)
    energy, attenuation_level = samples.T
    min_energy, max_energy = np.min(energy), np.max(energy)

    # Create cubic spline interpolation
    energy_estimate = np.linspace(min_energy, max_energy, 1000)
    attentuation_level_interpolation = interp1d(energy, attenuation_level, kind="cubic")
    attentuation_level_estimate = attentuation_level_interpolation(energy_estimate)

    # Calculate the attenuation coefficient for a photon with 4.65 MeV
    energy_value = 4.65
    attenuation = attentuation_level_interpolation(energy_value)
    print(
        f"The attenuation coefficient for a photon with 4.65 MeV energy is {attenuation:.5} cm^(-1)"
    )

    # Calculate percent of photons passing through the shield
    percent_photons = percent(attenuation)
    print(
        f"The percent of photos passing through a 2 cm thick lead shield is {percent_photons:.5%}"
    )

    # Plot scatter plot and the cubic spline interpolation
    plt.figure(Path(__file__).name)
    plt.scatter(energy, attenuation_level, zorder=3)
    plt.plot(energy_estimate, attentuation_level_estimate)

    # Provide title, axis labels, and scale of axis
    plt.title("Lead Attenuation Coefficient")
    plt.xlabel("Photon Energy [MeV]")
    plt.yscale("log")
    plt.ylabel(r"Attenuation level $\mu (cm^{-1})$")

    plt.show()


main()
