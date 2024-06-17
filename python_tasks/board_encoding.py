# board_encoding.py

"""
Decode an integer representation of a specific configuration for a Tic-Tac-Toe board given an integer in base 3 notation, printing out the decoded board
"""


# Helper function to convert a number to its base-three representation
def base_three(n):
    if n == 0:
        return "0"
    return_string = ""  # Create string to return value
    while n > 0:
        return_string = str(n % 3) + return_string
        n = n // 3
    return return_string


# Helper function to draw each board given an encoded integer
def draw_board(n):
    decoded = base_three(n)  # Change number into its base-three representation
    decoded = decoded[::-1]  # Reverse string
    while len(decoded) < 9:  # Add additional zeros, if necessary
        decoded = decoded + "0"

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]  # Initialize board and load in integer values
    for digit in range(0, 3):
        board[0][digit] = int(decoded[digit])
    for digit in range(0, 3):
        board[1][digit] = int(decoded[digit + 3])
    for digit in range(0, 3):
        board[2][digit] = int(decoded[digit + 6])

    print(f"Board Number: {n}")  # Print out board
    for row in range(3):
        print(board[row])


def main():
    boards_to_print = [2271, 1638, 12065]  # Put in encoded board numbers to print
    for board in boards_to_print:
        draw_board(board)


main()
