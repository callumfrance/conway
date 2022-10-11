from functools import reduce

from .board import board


def cell(cell_state: int = 0):
    # TODO fill in this function to process alive or dead computation
    # depending on what the state of the cell is
    pass


def process_alive():
    # TODO fill in this function to check the 'alive' conditions of a cell
    pass


def process_dead():
    # TODO fill in this function to check the 'dead' conditions of a cell
    pass


def _get_neighbours(board: list[list[int]], x: int, y: int) -> list[list[int]]:
    neighbours = list()
    upper_boundaries = (len(board), len(board[0]))

    def add_to_neighbours(lat, lng):
        return neighbours.append(board[lat][lng])

    if x != 0:
        if y != 0:
            add_to_neighbours(-1, -1)
        add_to_neighbours(-1, 0)
        if y != upper_boundaries[0]:
            add_to_neighbours(-1, 1)
    if x != upper_boundaries[1]:
        if y != 0:
            add_to_neighbours(1, -1)
        add_to_neighbours(1, 0)
        if y != upper_boundaries[0]:
            add_to_neighbours(1, 1)
    if y != 0:
        add_to_neighbours(0, -1)
    if y != upper_boundaries[0]:
        add_to_neighbours(0, 1)

    return neighbours


def get_neighbour_tally(board: list[list[int]], x: int, y: int) -> int:
    """Sums the list of neighbours and returns the result"""

    def sum_neighbours(current_result, next_value):
        """Function used in the reducer's computation"""
        return current_result + next_value

    # For more information on functools.reduce() -
    #    @See https://docs.python.org/3/library/functools.html#functools.reduce
    return reduce(sum_neighbours, _get_neighbours(board, x, y))


if __name__ == "__main__":
    print(_get_neighbours(board, 1, 1))
    print(get_neighbour_tally(board, 1, 1))
