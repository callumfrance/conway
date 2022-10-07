from cell import get_neighbour_tally


def check_overpopulation(board: list[list[int]], x: int, y: int) -> bool:
    """Any live cell with more than three live neighbours dies, as if by overpopulation.
    """
    pass


if __name__ == "__main__":
    demo_board_a = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 0],
    ]
    print(check_overpopulation(demo_board_a, 1, 1))

    demo_board_b = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
    ]
    print(check_overpopulation(demo_board_b, 1, 1))
