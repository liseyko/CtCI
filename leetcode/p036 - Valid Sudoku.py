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
