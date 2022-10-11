from os import system

from .board import board


def process_one_tick(board: list[list[int]]):
    # TODO fill in this function to iterate over every cell in every
    # row and column, processing whether it will be alive or dead,
    # and updating the board appropriately
    pass


def run():
    """Loops over the program forever.
    Press any key to continue to the next 'tick'
    """
    while True:
        system("clear")
        print_board(board)
        input()


def print_board(board: list[list[int]]):
    """Prints the board to stdout"""
    length = len(board[0])
    for row_index, row in enumerate(board):
        if row_index == 0:
            print("+ - - - - - +")
        if row_index <= 4:
            print("|", end=" ")
        for item in row:
            print(str(item), end=" ")
        if row_index <= 4:
            print("|", end=" ")
        if row_index == length - 1:
            print()
            print("+ - - - - - +")
        print()
