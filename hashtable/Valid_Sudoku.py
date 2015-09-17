# encoding=UTF-8
__author__ = 'Vincent'

'''

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''


class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        # check in line
        for line in board:
            numbers = {}
            for i in range(9):
                if line[i] != ".":
                    if not numbers.has_key(line[i]):
                        numbers[line[i]] = True
                    else:
                        return False
        #check in column
        for i in range(9):
            numbers = {}
            for j in range(9):
                if board[j][i] != ".":
                    if not numbers.has_key(board[j][i]):
                        numbers[board[j][i]] = True
                    else:
                        return False
        #check in block
        for row in range(3):
            for col in range(3):
                numbers = {}
                for i in range(3 * row, 3 * row + 3):
                    for j in range(3 * col , 3 * col + 3):
                        if board[i][j] != ".":
                            if not numbers.has_key(board[i][j]):
                                numbers[board[i][j]] = True
                            else:
                                return False
        return True


solution = Solution()
print solution.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])