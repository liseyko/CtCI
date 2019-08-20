class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows = [[0, 0] for _ in range(n)]
        self.cols = [[0, 0] for _ in range(n)]
        self.diag1, self.diag2 = [0, 0], [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        self.rows[col][player-1] += 1
        if self.rows[col][player-1] == self.n:
            return player

        self.cols[row][player-1] += 1
        if self.cols[row][player-1] == self.n:
            return player

        if row == col:
            self.diag1[player-1] += 1
            if self.diag1[player-1] == self.n:
                return player

        if row == self.n-1-col:
            self.diag2[player-1] += 1
            if self.diag2[player-1] == self.n:
                return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
