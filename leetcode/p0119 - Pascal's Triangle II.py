class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1, 1]
        for i in range(2, rowIndex+1):
            res = [1] + [res[j-1]+res[j] for j in range(1, i)] + [1]
        return res[:rowIndex+1]

    def getRow(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row

    def getRow(self, rowIndex):
        row = [1]
        for k in range(rowIndex):
            row.append(1)
            for i in range(k, 0, -1):
                row[i] = row[i] + row[i-1]
        return row

    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1, rowIndex+1):
            for j in range(i//2, 0, -1):
                res[j] = res[i-j] = res[j] + res[j-1]
            res.append(1)
        return res
