from .cell import cell

# @see https://stackoverflow.com/a/58584557
# fmt: off
board = [
    [0, 0, 0, 0, 1, ],
    [0, 0, 0, 0, 0, ],
    [0, 0, 1, 0, 0, ],
    [0, 1, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
]
# fmt: on


def test_cell():
    actual = cell(board, 2, 1)
    expected = 0

    assert actual == expected


def test_cell_alive():
    actual = cell(board, 0, 4)
    expected = None

    assert actual == expected
