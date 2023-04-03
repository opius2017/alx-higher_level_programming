#!/usr/bin/python3
import sys


def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        return 1
    if N < 4:
        print("N must be at least 4")
        return 1

    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i]:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j]:
                return False
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j]:
                return False
        return True

    def solve(board, col, solutions):
        if col == N:
            solution = []
            for i in range(N):
                row = [0] * N
                for j in range(N):
                    if board[i][j]:
                        row[j] = 1
                solution.append(row)
            solutions.append(solution)
            return
        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve(board, col + 1, solutions)
                board[i][col] = 0

    board = [[0] * N for i in range(N)]
    solutions = []
    solve(board, 0, solutions)
    for solution in solutions:
        for row in solution:
            print(' '.join(str(x) for x in row))
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    exit_code = nqueens(N)
    sys.exit(exit_code)
