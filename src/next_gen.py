from cell import get_neighbour_tally


def check_next_gen(board: list[list[int]], x: int, y: int) -> bool:
    """Any live cell with two or three live neighbours lives
    on to the next generation
    """
    return (
        get_neighbour_tally(board, x, y) == 2 or get_neighbour_tally(board, x, y) == 3
    )


if __name__ == "__main__":
    demo_board_a = [
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 0],
    ]
    print(check_next_gen(demo_board_a, 1, 1))

    demo_board_b = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 0],
    ]
    print(check_next_gen(demo_board_b, 1, 1))
