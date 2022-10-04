from board import board


def run():
    print_board_alternate(board)


def print_board_alternate(board: list[list[int]]):
    """Another way of printing the board"""
    length = len(board[0])
    for row_index, row in enumerate(board):
        if row_index == 0:
            print("+")
        for item in row:
            print(str(item), end=" ")
        if row_index == length - 1:
            print("+")
        print()
