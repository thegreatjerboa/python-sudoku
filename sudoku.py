from enum import Enum


BoardStatus = Enum('BoardStatus', 'solved invalid partial')

def main():
    board = [[0, 0, 0,  0, 0, 0,  0, 0, 0],
             [3, 1, 0,  0, 0, 0,  0, 2, 8],
             [0, 0, 9,  8, 0, 2,  6, 0, 0],

             [1, 9, 6,  0, 0, 0,  5, 4, 7],
             [8, 5, 0,  1, 0, 4,  0, 6, 9],
             [0, 0, 0,  0, 0, 0,  0, 0, 0],

             [0, 0, 0,  0, 0, 0,  0, 0, 0],
             [9, 4, 0,  0, 0, 0,  0, 5, 3],
             [0, 3, 7,  0, 2, 0,  4, 8, 0]]
    printBoard(board)
    # print(getRow(board, 1))
    # print(flatenBoard(board))
    # print(getCol(board, 1))
    # print()
    # print(getSquare(board, 0))
    # print(getSquare(board, 1))
    # print(getSquare(board, 2))
    # print(getSquare(board, 3))
    # print(getSquare(board, 4))
    # print(getSquare(board, 5))
    # print(getSquare(board, 6))
    # print(getSquare(board, 7))
    # print(getSquare(board, 8))
    # print()
    # print(validateSegement(range(0, 9)))
    # print(validateSegement(range(1, 10)))
    # print(validateSegement([0, 0, 0,  0, 0, 0,  0, 1, 1]))
    solveBoard(board)


def solveBoard(board):
    status = validateBoard(board)
    if status == BoardStatus.invalid:
        return
    elif status == BoardStatus.solved:
        printBoard(board)
    else:
        newBoard = [row[:] for row in board]
        for rowNum, line in enumerate(board):
            for colNum, cell in enumerate(line):
                if cell == 0:
                    for b in range(1,10):
                        newBoard[rowNum][colNum] = b
                        solveBoard(newBoard)
                    return


def validateBoard(board):
    status = [validateSegement(seg) for seg in sum([[getRow(board, i), getCol(board, i), getSquare(board, i)]for i in range(0, 9)], [])]
    # print(status)
    if all([item == BoardStatus.solved for item in status]):
        return BoardStatus.solved
    return BoardStatus.invalid if any([item == BoardStatus.invalid for item in status]) else BoardStatus.partial


def validateSegement(segment):
    seen = set()
    seen_add = seen.add
    for item in [item for item in segment if item != 0]:
        if item in seen:
            return BoardStatus.invalid
        else:
            seen_add(item)
    # print(seen)
    return BoardStatus.solved if len(seen) == 9 else BoardStatus.partial


def getRow(board, row):
    return board[row]


def flatenBoard(board):
    return sum(board, [])


def getCol(board, col):
    return flatenBoard(board)[col:9*9:9]


def getSquare(board, num):
    mod = 3*(num % 3)
    div = 3*(num // 3)
    return sum([line[0+mod:3+mod] for line in board[0+div:3+div]], [])


def printBoard(board):
    print(validateBoard(board))
    for i, line in enumerate(board):
        if i % 3 == 0:
            print()
        printLine(line)


def printLine(line):
    for i, cell in enumerate(line):
        if i % 3 == 0:
            print(" ", end="")
        print(cell, end="")
    print()


if __name__ == '__main__':
    main()

