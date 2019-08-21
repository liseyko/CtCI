class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def get_neighbours(x, y):
            r = []
            for j in (y-1, y+1):
                if -1 < j < h:
                    r.append((j, x))
            for i in (x-1, x+1):
                if -1 < i < w:
                    r.append((y, i))
            return r

        def bt(y, x, k=1, vis=set()):
            if k == wl:
                return True
            for (j, i) in get_neighbours(x, y):
                if (j, i) not in vis and board[j][i] == word[k]:
                    vis.add((y, x))
                    if bt(j, i, k+1, vis):
                        return True
                    vis.remove((y, x))
            return False

        h = len(board)
        w = len(board[0]) if h else 0
        wl = len(word)

        for j in range(h):
            for i in range(w):
                if board[j][i] == word[0] and bt(j, i):
                    return True

        return False
