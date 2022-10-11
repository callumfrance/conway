from cell import get_neighbour_tally


def check_underpopulation(board: list[list[int]], x: int, y: int) -> bool:
    """Any live cell with fewer than two live neighbours dies,
    as if by underpopulation.
    """
    return get_neighbour_tally(board, x, y) < 2


if __name__ == "__main__":

    print(check_underpopulation(demo_board_a, 1, 1))

    print(check_underpopulation(demo_board_b, 1, 1))
