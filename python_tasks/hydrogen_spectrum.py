# hydrogen_spectrum.py

"""
Calculates and displays the wavelengths (in nanometers) for both the Pfund and Humphreys high energy spectral series of Hydrogen
Calculate and display the wavelengths for both series using both Rydberg and Bohr formulas
"""


# Helper function to compute the wavelength with the Rydberg formula
def rydberg_formula(initial_orbit, final_orbit):
    rydberg_constant = 1.0967757e7
    inverse = rydberg_constant * ((1 / (final_orbit**2)) - (1 / (initial_orbit**2)))
    if inverse == 0:
        return float("inf")  # To handle divide by zero issue
    return (1 / inverse) * 1e9  # convert meters to nanometers


# Helper function to compute the wavelength with the Bohr formula
def bohr_formula(initial_orbit, final_orbit):
    h_plank = 6.626e-34
    speed_light = 2.998e8
    e_mass = 9.109e-31
    e_charge = 1.602e-19
    permittivity = 8.854e-12

    # Bohr's formula for ground state energy
    e_0 = (e_charge**4 * e_mass) / (8 * permittivity**2 * h_plank**2)
    # Initial energy level
    e_i = -e_0 / initial_orbit**2
    # Final energy level
    e_f = -e_0 / final_orbit**2

    # Formula for waveLength in nanometers
    wave_length = h_plank * speed_light / (e_i - e_f) * 1e9
    return wave_length


def main():
    # Print out Pfund series
    final_orbit = 5
    print("Pfund series:")
    print("Rydberg formula:")
    for initial_orbit in range(6, 11):
        rydberg_wavelength = rydberg_formula(initial_orbit, final_orbit)
        print(f"{initial_orbit:>2} -> {final_orbit:>2} : {rydberg_wavelength:8.0f} nm")
    print("Bohr formula:")
    for initial_orbit in range(6, 11):
        bohr_wavelength = bohr_formula(initial_orbit, final_orbit)
        print(f"{initial_orbit:>2} -> {final_orbit:>2} : {bohr_wavelength:8.0f} nm")

    # Print out Humphreys series
    final_orbit = 6
    print("Humphreys series:")
    print("Rydberg formula:")
    for initial_orbit in range(7, 12):
        rydberg_wavelength = rydberg_formula(initial_orbit, final_orbit)
        print(f"{initial_orbit:>2} -> {final_orbit:>2} : {rydberg_wavelength:8.0f} nm")
    print("Bohr formula:")
    for initial_orbit in range(7, 12):
        bohr_wavelength = bohr_formula(initial_orbit, final_orbit)
        print(f"{initial_orbit:>2} -> {final_orbit:>2} : {bohr_wavelength:8.0f} nm")


main()
