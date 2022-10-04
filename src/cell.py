from conway import board


def cell(cell_state: int = 0):
    pass


def get_neighbours(board: list[list[int]], x: int, y: int) -> list[list[int]]:
    neighbours = list()
    upper_boundaries = (len(board), len(board[0]))

    def add_to_neighbours(lat, lng): return neighbours.append(board[lat][lng])

    if x != 0:
        if y != 0:
            add_to_neighbours(-1, -1)
        add_to_neighbours(-1, 0)
        if y != upper_boundaries[0]:
            add_to_neighbours(-1, 1)
    if x != upper_boundaries[1]:
        if y != 0:
            add_to_neighbours(1, -1)
        add_to_neighbours(1, 0)
        if y != upper_boundaries[0]:
            add_to_neighbours(1, 1)
    if y != 0:
        add_to_neighbours(0, -1)
    if y != upper_boundaries[0]:
        add_to_neighbours(0, 1)

    return(neighbours)


if __name__ == '__main__':
    print(get_neighbours(board, 1, 1))
