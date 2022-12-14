import pytest
from .cell import process_alive, process_dead, cell

# @see https://stackoverflow.com/a/58584557
# fmt: off
board = [
    [0, 0, 0, 0, 1, ],
    [0, 0, 1, 1, 0, ],
    [0, 1, 1, 0, 0, ],
    [0, 1, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
]


demo_board_a = [
    [0, 0, 0],
    [0, 1, 1],
    [0, 1, 0],
]

demo_board_b = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
]

demo_board_c = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 1]
]
# fmt: on


def test_cell():
    actual = cell(board, 2, 1)
    expected = 1

    assert actual == expected


@pytest.mark.parametrize(
    "input_board, input_x, input_y, expected",
    [
        (demo_board_a, 1, 1, 1),
        (demo_board_a, 1, 2, 1),
        (demo_board_a, 0, 0, 0),
        (demo_board_b, 1, 1, 0),
        (demo_board_c, 1, 0, 0),
    ],
)
def test_cell_alive(input_board, input_x, input_y, expected):
    assert process_alive(input_board, input_x, input_y) == expected


@pytest.mark.parametrize(
    "input_board, input_x, input_y, expected",
    [
        (demo_board_a, 1, 1, 0),
        (demo_board_a, 1, 2, 0),
        (demo_board_a, 0, 0, 0),
        (demo_board_b, 0, 0, 1),
        (demo_board_c, 1, 0, 0),
    ],
)
def test_cell_dead(input_board, input_x, input_y, expected):
    assert process_dead(input_board, input_x, input_y) == expected
