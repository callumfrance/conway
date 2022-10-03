import numpy as np

board = [
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
]


def run():
    print(board)
    print_board(board,5)

def print_board(board1,n):
    arr = np.array(board1)
    arr = arr.reshape(5,5)
    print(str(arr).replace(" [","").replace("[","").replace("]",""))
    pass



if __name__ == '__main__':
    run()
