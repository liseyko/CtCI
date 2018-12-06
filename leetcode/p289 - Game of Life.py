class Solution:
    def gameOfLife(self, board):
        """
        Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population..
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.m, self.n = len(board[0]), len(board)
        def getNoN(i0,j0):
            r = 0 
            for j in range(j0-1,j0+2):
                if -1 < j < self.n:
                    for i in range(i0-1,i0+2):
                        if  -1 < i < self.m and (i,j) != (i0,j0):
                            r += board[j][i] % 10
            return r
        
        for j in range(self.n):
            for i in range(self.m):
                n = getNoN(i,j)
                if (n == 3 and not board[j][i] % 10) or \
                (board[j][i] % 10 and (n < 2 or n > 3)):
                    board[j][i] = (1 - board[j][i]) * 10 + board[j][i]
                else:
                    board[j][i] = board[j][i]*10 + board[j][i]
        for j in range(self.n):
            for i in range(self.m):
                board[j][i] //= 10
                
    def gameOfLife(self, board):
        self.m, self.n = len(board[0]), len(board)
        def getNoN(i0,j0):
            r = 0 
            for j in range(j0-1,j0+2):
                if -1 < j < self.n:
                    for i in range(i0-1,i0+2):
                        if  -1 < i < self.m and (i,j) != (i0,j0):
                            r += board[j][i] & 1
            return r
        
        for j in range(self.n):
            for i in range(self.m):
                n = getNoN(i,j)
                if (n == 3 and not board[j][i] & 1) or \
                (board[j][i] & 1 and (n < 2 or n > 3)):
                    board[j][i] = ((1 - board[j][i]) << 1) + board[j][i]
                else:
                    board[j][i] = (board[j][i] << 1) + board[j][i]
        
        for j in range(self.n):
            for i in range(self.m):
                board[j][i] >>= 1