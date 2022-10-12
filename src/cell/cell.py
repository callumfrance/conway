from ..reproduction import check_reproduction


def cell(board: list[list[int]], x: int, y: int) -> int:
    # TODO fill in this function to process alive or dead computation
    # depending on what the state of the cell is
    test_cell = board[x][y]

    if test_cell == 0:
        return process_dead(board, x, y)
    else:
        return process_alive(board, x, y)


def process_alive(board: list[list[int]], x: int, y: int):
    # TODO fill in this function to check the 'alive' conditions of a cell
    pass


def process_dead(board: list[list[int]], x: int, y: int) -> int:
    # fill in this function to check the 'dead' conditions of a cell
    live = check_reproduction(board, x, y)
    if live:
        return 1
    else:
        return 0
