import pytest

from .get_neighbour_tally import get_neighbour_tally

# fmt: off
demo_board = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
]
# fmt: on

a = [[0, 1], [0, 0]]
b = [[0, 0], [0, 0]]
c = [[0, 0], [1, 0]]
d = [[0, 0], [0, 0]]


@pytest.mark.parametrize(
    "input_board, input_x, input_y, expected",
    [
        (a, 0, 0, 1),
        (b, 0, 0, 0),
        (c, 1, 1, 1),
        (d, 1, 1, 0),
        (demo_board, 1, 1, 3),
        (demo_board, 0, 1, 2),
        (demo_board, 1, 0, 3),
        (demo_board, 0, 0, 2),
        (demo_board, 2, 2, 3),
    ],
)
def test_get_neighbour_tally(input_board, input_x, input_y, expected):
    assert get_neighbour_tally(input_board, input_x, input_y) == expected
