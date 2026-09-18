from collections import defaultdict


def is_valid_sudoku(board):
    size = 9
    columns = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    for row in range(size):
        for col in range(size):
            cell = board[row][col]

            if cell == ".":
                continue

            if cell in columns[col] or cell in rows[row] or cell in squares[(row // 3, col // 3)]:
                return False

            squares[(row // 3, col // 3)].add(cell)
            columns[col].add(cell)
            rows[row].add(cell)

    return True


if __name__ == '__main__':
    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(is_valid_sudoku(board))  # expected: True

    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "1", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(is_valid_sudoku(board))  # expected: False (two 1s in top-left box)
