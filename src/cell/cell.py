from ..reproduction import check_reproduction
from ..underpopulation import check_underpopulation
from ..overpopulation import check_overpopulation
from ..next_gen import check_next_gen


def cell(board: list[list[int]], x: int, y: int) -> int:
    """The function inputs the board which is list of list of integers,
    x and y as coordinates and returns an integer 0 which is dead cell or 1 which is
    a live cell"""
    test_cell = board[x][y]

    if test_cell == 0:
        return process_dead(board, x, y)
    else:
        return process_alive(board, x, y)


def process_alive(board: list[list[int]], x: int, y: int) -> int:
    # TODO fill in this function to check the 'alive' conditions of a cell
    is_underpopulated = check_underpopulation(board, x, y)
    is_nextgen = check_next_gen(board, x, y)
    is_overpopulated = check_overpopulation(board, x, y)

    if is_nextgen and not (is_underpopulated or is_overpopulated):
        return 1
    else:
        return 0


def process_dead(board: list[list[int]], x: int, y: int) -> int:
    # fill in this function to check the 'dead' conditions of a cell
    live = check_reproduction(board, x, y)
    if live:
        return 1
    else:
        return 0
