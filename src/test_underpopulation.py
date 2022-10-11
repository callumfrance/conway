import pytest

from .underpopulation import check_underpopulation

demo_board_a = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0],
]

demo_board_b = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 1, 0],
]


@pytest.mark.parametrize(
    "input_board, input_x, input_y, expected",
    [
        (demo_board_a, 1, 1, False),
        (demo_board_a, 0, 0, True),
        (demo_board_b, 0, 1, True),
        (demo_board_b, 1, 0, False),
    ],
)
def test_underpopulation(input_board, input_x, input_y, expected):
    assert check_underpopulation(input_board, input_x, input_y) == expected
