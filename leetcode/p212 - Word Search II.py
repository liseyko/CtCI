class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return []
        h, w = len(board), len(board[0])

        def getpaths(y, x):
            paths = []
            for j in (y-1, y+1):
                if -1 < j < h and (j, x) not in vis:
                    paths.append((j, x))
            for i in (x-1, x+1):
                if -1 < i < w and (y, i) not in vis:
                    paths.append((y, i))
            return paths

        def dfs(y, x, t, cw=[]):
            for c in t:
                if c == board[y][x]:
                    vis.add((y, x))
                    cw.append(c)
                    if '\n' in t[c]:
                        self.res.add(''.join(cw))
                    for (j, i) in getpaths(y, x):
                        dfs(j, i, t[c], cw)
                    vis.remove((y, x))
                    cw.pop()

        trie = {}
        vis = set()
        for word in words:
            for c in word:
                t = trie
                for c in word:
                    if c in t:
                        t = t[c]
                    else:
                        t[c] = {}
                        t = t[c]
                t['\n'] = None

        self.res = set()
        for j in range(h):
            for i in range(w):
                dfs(j, i, trie)

        return list(self.res)
