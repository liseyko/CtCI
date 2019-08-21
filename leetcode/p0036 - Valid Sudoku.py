class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = [set() for _ in range(9)]
        for row in range(9):
            if not row % 3:
                squares = set(),set(),set()
            cur_row = set()
            for col in range(9):
                if board[row][col] == '.': continue
                for s in cur_row, cols[col], squares[col // 3]:
                    if board[row][col] in s: 
                        return False
                    else: 
                        s.add(board[row][col])
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """                
        rows, cols = [set() for _ in range(9)], [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]
        for j, row in enumerate(board):
            for i, col in enumerate(row):
                if board[j][i] != '.':
                    if board[j][i] in rows[j] | cols[i] | squares[j // 3][i // 3]:
                        return False
                    rows[j].add(board[j][i])
                    cols[i].add(board[j][i])
                    squares[j//3][i//3].add(board[j][i])

        return True