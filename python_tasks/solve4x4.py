# solve4x4.py

import numpy as np

"""
Display solution to the following system of linear equations:
    x1 + 2x2 + x3 - x4 = 5
    3x1 + 2x2 + 4x3 + 4x4 = 16
    4x1 + 4x2 + 3x3 + 4x4 = 22
    2x1 + x3 + 5x4 = 15
Does this by utilizing Cramer's Rule and then numpy's linear algebra capabilities
"""


def main():
    # Utilizing Cramer's Rule, generating each overlay matrix
    matrix = np.array([[1, 2, 1, -1], [3, 2, 4, 4], [4, 4, 3, 4], [2, 0, 1, 5]])
    x_1 = np.array([[5, 2, 1, -1], [16, 2, 4, 4], [22, 4, 3, 4], [15, 0, 1, 5]])
    x_2 = np.array([[1, 5, 1, -1], [3, 16, 4, 4], [4, 22, 3, 4], [2, 15, 1, 5]])
    x_3 = np.array([[1, 2, 5, -1], [3, 2, 16, 4], [4, 4, 22, 4], [2, 0, 15, 5]])
    x_4 = np.array([[1, 2, 1, 5], [3, 2, 4, 16], [4, 4, 3, 22], [2, 0, 1, 15]])

    # Determine determinant for each of the matrices
    matrix_determinant = np.linalg.det(matrix)
    x_1_determinant = np.linalg.det(x_1)
    x_2_determinant = np.linalg.det(x_2)
    x_3_determinant = np.linalg.det(x_3)
    x_4_determinant = np.linalg.det(x_4)

    # Use determinants to calculate values
    x_1_value = x_1_determinant / matrix_determinant
    x_2_value = x_2_determinant / matrix_determinant
    x_3_value = x_3_determinant / matrix_determinant
    x_4_value = x_4_determinant / matrix_determinant

    # Print results
    print(
        f"The solution to the system is x1 = {x_1_value:.4}, x2 = {x_2_value:.4}, x3 = {x_3_value:.4}, and x4 = {x_4_value:.4}."
    )

    # Solve using numpy's linear algebra library
    solutions = np.array([5, 16, 22, 15])
    answer = np.linalg.solve(matrix, solutions)

    # Print results again
    print(
        f"The solution to the system is x1 = {answer[0]}, x2 = {answer[1]}, x3 = {answer[2]}, and x4 = {answer[3]}."
    )


main()
