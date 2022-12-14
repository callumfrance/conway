from functools import reduce

from ..board import board


def _get_neighbours(board: list[list[int]], x: int, y: int) -> list[list[int]]:
    neighbours = list()
    upper_boundaries = (len(board) - 1, len(board[0]) - 1)

    def add_to_neighbours(lat, lng):
        return neighbours.append(board[x + lat][y + lng])

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
    return reduce(sum_neighbours, _get_neighbours(board, x, y), 0)


if __name__ == "__main__":
    print(_get_neighbours(board, 1, 1))
    print(get_neighbour_tally(board, 1, 1))
