import numpy as np

board = [
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
    [0, 1, 0, 0, 0, ],
    [1, 0, 0, 0, 0, ],
]


def run():
    print(board)
    #print_board(board)
    print_board_alternate(board)


def print_board(board1):
    arr = np.array(board1)
    print(arr)
    arr = arr.reshape(5, 5)
    print(arr)
    print(str(arr).replace(" [", "").replace("[", "").replace("]", ""))


def print_board_alternate(board: list[list[int]]):
    """Another way of printing the board
    """
    for row in board:
        for item in row:
            print(str(item), end=' ')
        print()



