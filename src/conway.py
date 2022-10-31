from os import system

from .board import board

from src.cell.cell import cell


def process_one_tick(board: list[list[int]]) -> list[list[int]]:
    # TODO fill in this function to iterate over every cell in every
    # row and column, processing whether it will be alive or dead,
    # and updating the board appropriately
    output: list[list[int]] = []

    for row_index, row in enumerate(board):
        output_row: list[int] = []

        for cell_index, _ in enumerate(row):
            output_row.append(cell(board, row_index, cell_index))

        output.append(output_row)

    return output


def run():
    """Loops over the program forever.
    Press any key to continue to the next 'tick'
    """
    current_board = board

    while True:
        system("clear")
        print_board(current_board)
        current_board = process_one_tick(current_board)

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
            print(mask_cell(item), end=" ")
        if row_index <= 4:
            print("|", end=" ")
        if row_index == length - 1:
            print()
            print("+ - - - - - +")
        print()


def mask_cell(item, alive="@", dead=".") -> str:
    """Masks the alive/dead cells with any string you want.
    By default '@' for alive and '.' for dead"""
    return alive if item == 1 else dead
