class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        row = [1, 1]
        for _ in range(1, rowIndex):
            row.append(1)
            if len(row) % 2:
                row[len(row) // 2] = row[len(row) // 2] + row[len(row) // 2 - 1]
            for i in range(len(row) // 2 - 1, 0, -1):
                row[i] = row[i] + row[i-1]
                row[-i-1] = row[i]

        return row

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
