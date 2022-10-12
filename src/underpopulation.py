from .cell.get_neighbour_tally import get_neighbour_tally


def check_underpopulation(board: list[list[int]], x: int, y: int) -> bool:
    """Any live cell with fewer than two live neighbours dies,
    as if by underpopulation.
    """
    return get_neighbour_tally(board, x, y) < 2
