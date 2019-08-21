class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        r = [[] for _ in range(numRows)]
        i = 0
        while i < len(s):
            zig = 0
            while i < len(s) and zig < numRows:
                r[zig].append(s[i])
                i, zig = i + 1, zig + 1

            zag = numRows - 2
            while i < len(s) and zag > 0:
                r[zag].append(s[i])
                i, zag = i + 1, zag - 1

        return ''.join([''.join(s) for s in r])

    # line-by-line approach:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        res, rowNum = [], 0
        jump1, jump2 = numRows * 2 - 4, 2
        while rowNum < numRows:
            if rowNum == 0 or rowNum == numRows - 1:
                i = rowNum
                while i < len(s):
                    res.append(s[i])
                    i += numRows * 2 - 2
                rowNum += 1
                continue

            i, curJump = rowNum, jump1
            while i < len(s):
                res.append(s[i])
                i += curJump
                curJump = jump2 if curJump == jump1 else jump1
            rowNum, jump1, jump2 = rowNum + 1, jump1 - 2, jump2 + 2
        return ''.join(res)

    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if numRows < 2:
            return s
        res, step = [], numRows*2-2
        for row_i in range(numRows):
            for zig in range(row_i, len(s), step):
                res.append(s[zig])
                if 0 < row_i < numRows-1:
                    zag = zig + 2*(numRows-row_i-1)
                    if zag < len(s):
                        res.append(s[zag])
        return ''.join(res)
