class Sudoku():
    def __init__(self, board):
        self.board = board
        self.nums = {chr(i + ord('1')) for i in range(9)}
        self.rows = {i : set() for i in range(9)}
        self.cols = {i : set() for i in range(9)}
        self.sqrs = {(i,j) : set() for i in range(3) for j in range(3)} 
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == '.': continue
                self.rows[i].add(col)
                self.cols[j].add(col)
                self.sqrs[(i//3,j//3)].add(col)

    def add(self, i, j, n):
            self.rows[i].add(n)
            self.cols[j].add(n)
            self.sqrs[(i//3,j//3)].add(n)
            self.board[i][j] = n

    def safeadd(self, i, j, n):
            if n in self.rows[i] or n in self.cols[j] or n in self.sqrs[(i//3,j//3)]:
                return False
            self.add(i,j,n)
            return True

    def rm(self, i, j, n):
            self.rows[i].discard(n)
            self.cols[j].discard(n)
            self.sqrs[(i//3,j//3)].discard(n)
            self.board[i][j] = '.'
            
    def options(self, i, j):
        return self.nums - self.rows[i] - self.cols[j] - self.sqrs[(i//3,j//3)]

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board, self.solved = board, False
        s = Sudoku(board)

        def bt(i=0, j=0):
            if j > 8:
               i, j = i + 1, 0
            if i > 8:
                self.solved = True
            else:
                if self.board[i][j] != '.': return bt(i, j+1)
                opts = s.options(i, j)
                if not opts: return
                for n in opts:
                    s.add(i, j, n)
                    bt(i, j+1)
                    if self.solved: return
                    s.rm(i, j, n)

        bt()
