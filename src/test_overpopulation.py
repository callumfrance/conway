import pytest

from .overpopulation import check_overpopulation

_test_board_a = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
]

_test_board_b = [
    [0, 0, 0],
    [0, 1, 1],
    [0, 1, 0],
]


@pytest.mark.parametrize(
    "input_board, input_x, input_y, expected",
    [
        (_test_board_a, 1, 1, True),
        (_test_board_a, 0, 0, False),
        (_test_board_b, 1, 1, False),
        (_test_board_b, 2, 2, False),
    ],
)
def test_overpopulation(input_board, input_x, input_y, expected):
    assert check_overpopulation(input_board, input_x, input_y) == expected
