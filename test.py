board = [
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, ],
    [0, 1, 0, 0, 0, ],
    [1, 0, 0, 0, 0, ],
]


# for x in range(len(board)):
#     for y in range(len(board[x])):
#         print(board[x][y])

for row_index,row in enumerate(board):
        for cell_index, item in enumerate(row):
            print(row_index, cell_index)
    