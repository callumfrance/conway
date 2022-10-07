from cell import get_neighbour_tally


def check_reproduction(board: list[list[int]], x: int, y: int) -> bool:
    """Any dead cell with exactly three live neighbours becomes a live cell,
     as if by reproduction.
    """
    return get_neighbour_tally(board, x, y) == 3


if __name__ == "__main__":
    demo_board_a = [
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 0],
    ]
    print(check_reproduction(demo_board_a, 1, 1))

    demo_board_b = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 0],
    ]
    print(check_reproduction(demo_board_b, 1, 1))
