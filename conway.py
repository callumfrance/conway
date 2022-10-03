board = [
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
]


def run():
    print(board)
    print_board(board)

def print_board(board1):
    for row in board1:
        for x in row:
            print(x, end=' ')
    pass



if __name__ == '__main__':
    run()
