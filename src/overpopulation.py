from .cell.get_neighbour_tally import get_neighbour_tally


def check_overpopulation(board: list[list[int]], x: int, y: int) -> bool:
    """Any live cell with more than three live neighbours dies,
    as if by overpopulation."""
    return get_neighbour_tally(board, x, y) > 3
