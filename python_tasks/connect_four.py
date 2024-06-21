# connect_four.py


def check_winner(player, board):
    """
    Takes the player number and the board and iteratively checks each position.
    Looks to make sure the space 4 to the right, bottom, bottom-right diagonal, and bottom-left diagonal spaces are in bounds.
    Checks to see if all spaces in between the two coordinates have the player in them.
    Break if a win is found.
    """
    found = False

    for row in range(len(board)):  # Nested for loops to iterate through each spot
        for col in range(len(board[0])):
            # Right
            if col + 3 < len(board[0]) and all(
                board[row][col + i] == player for i in range(4)
            ):
                found = True
                break
            # Bottom
            if row + 3 < len(board) and all(
                board[row + i][col] == player for i in range(4)
            ):
                found = True
                break
            # Bottom-right diagonal
            if (
                col + 3 < len(board[0])
                and row + 3 < len(board)
                and all(board[row + i][col + i] == player for i in range(4))
            ):
                found = True
                break
            # Bottom-left diagonal
            if (
                col - 3 >= 0
                and row + 3 < len(board)
                and all(board[row + i][col - i] == player for i in range(4))
            ):
                found = True
                break

        # If a win has been detected, we can stop iterating
        if found:
            break

    return found


def print_winner(board):
    print(*board, sep="\n")
    if check_winner(1, board):
        print("Player 1 wins!")
    else:
        if check_winner(2, board):
            print("Player 2 wins!")
        else:
            print("No winner yet")
    print()


def main():
    board1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2 = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


main()
