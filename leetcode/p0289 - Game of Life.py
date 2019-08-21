class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def getN(y, x):
            n = 0 - board[y][x] % 10
            for j in range(max(0, y-1), min(len(board), y+2)):
                for i in range(max(0, x-1), min(len(board[j]), x+2)):
                    n += board[j][i] % 10
            return n

        for j, row in enumerate(board):
            for i, cell in enumerate(row):
                n = getN(j, i)
                if cell and (n < 2 or n > 3)\
                   or n == 3 and not cell:
                    board[j][i] += 10

        for j, row in enumerate(board):
            for i, cell in enumerate(row):
                if cell > 9:
                    board[j][i] = abs(board[j][i] % 10 - board[j][i] // 10)

    def gameOfLife(self, board):
        self.m, self.n = len(board[0]), len(board)

        def getNoN(i0, j0):
            r = 0
            for j in range(j0-o1, j0+2):
                if -1 < j < self.n:
                    for i in range(i0-1, i0+2):
                        if -1 < i < self.m and (i, j) != (i0, j0):
                            r += board[j][i] & 1
            return r

        for j in range(self.n):
            for i in range(self.m):
                n = getNoN(i, j)
                if (n == 3 and not board[j][i] & 1) or\
                   (board[j][i] & 1 and (n < 2 or n > 3)):
                    board[j][i] = ((1 - board[j][i]) << 1) + board[j][i]
                else:
                    board[j][i] = (board[j][i] << 1) + board[j][i]

        for j in range(self.n):
            for i in range(self.m):
                board[j][i] >>= 1
