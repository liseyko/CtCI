class Solution:
    def __init__(self):
        self.pt = [[1], [1, 1]]

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        while numRows > len(self.pt):
            tail, newtail = self.pt[-1], [1]
            tl = len(tail)
            for i in range(1, tl // 2 + 1):
                newtail.append(tail[i-1] + tail[i])
            newtail.extend(newtail[tl // 2 - (tl + 1) % 2::-1])
            self.pt.append(newtail)

        return self.pt[:numRows]

    def generate(self, numRows):
        r = [[1], [1, 1]]
        for n in range(2, numRows):
            r.append([1] + [r[-1][i-1] + r[-1][i] for i in range(1, n)] + [1])

        return r[:numRows]
