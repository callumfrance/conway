from ..reproduction import check_reproduction


def cell(cell_state: int = 0):
    # TODO fill in this function to process alive or dead computation
    # depending on what the state of the cell is
    pass


def process_alive(board: list[list[int]], x: int, y: int):
    # TODO fill in this function to check the 'alive' conditions of a cell
    pass


def process_dead(board: list[list[int]], x: int, y: int) -> int:
    # fill in this function to check the 'dead' conditions of a cell
    dead = check_reproduction(board, x, y)
    if dead:
        return 1
    else:
        return 0
