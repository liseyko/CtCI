class TicTacToe(object):

    def __init__(self, n):
        self.n = n
        self.row, self.col = [0] * n, [0] * n
        self.diagLR = self.diagRL = 0

    def move(self, row, col, player):
        offset = player * 2 - 3
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diagLR += offset
        if row == self.n - 1 - col:
            self.diagRL += offset
        if offset * self.n in [self.row[row], self.col[col], self.diagLR, self.diagRL]:
            return player

        return 0


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [[0, 0] for _ in range(n)]
        self.cols = [[0, 0] for _ in range(n)]
        self.diag1, self.diag2 = [0, 0], [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        player -= 1
        self.rows[col][player] += 1
        self.cols[row][player] += 1
        if row == col:
            self.diag1[player] += 1
        if row == self.n-1-col:
            self.diag2[player] += 1

        if self.n in (self.rows[col][player], self.cols[row][player],
                      self.diag1[player], self.diag2[player]):
            return player+1

        return 0
