# rlc_circuit.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

"""
Plots the current over time flowing through an RLC circuit that maintains a constant DC voltage given initial conditions
"""


# Helper function to calculate dI_dt and d2I_dt2
def model(t, state_vector, R, C, L):
    current, dI_dt = state_vector
    d2I_dt2 = -(R / L) * dI_dt - (1 / (L * C)) * current
    return [dI_dt, d2I_dt2]


def main():
    # Parameters and initial conditions for RLC circuit
    R = 0.1  # Ohms
    C = 0.01  # Farads
    L = 0.01  # Henrys

    I0 = 1.0  # Amps
    dI_dt0 = 0.0  # Amps/second

    t_initial = 0  # Seconds
    t_final = 1  # Seconds
    t_range = np.linspace(t_initial, t_final, 1000)  # evaluation points

    # Solve differential equation given initial conditions
    sol = solve_ivp(
        model,
        (t_initial, t_final),
        [I0, dI_dt0],
        t_range=t_range,
        args=(R, C, L),
        max_step=0.001,
    )

    # Get time and current to plot
    time = sol.t
    current = sol.y[0]

    plt.figure(Path(__file__).name)

    # Set title and axis labels
    plt.plot(time, current)
    plt.title("Resistor-Inductor-Capacitor Circuit")
    plt.xlabel("Time (secs)")
    plt.ylabel("Current (Amps)")

    plt.show()


main()
