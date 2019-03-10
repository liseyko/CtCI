class Solution:
    def generate(self, numRows):
        r = [[1], [1, 1]]
        for n in range(2, numRows):
            r.append([1] + [r[-1][i-1] + r[-1][i] for i in range(1, n)] + [1])

        return r[:numRows]


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.res = [[1], [1, 1]] 
        for _ in range(2, numRows):
            self.res.append(self.generateNextRow())
            
        return self.res[:numRows]
            
    def generateNextRow(self):
        lastRow = self.res[-1]
        newRowMidPart = [lastRow[col-1] + lastRow[col] 
                         for col in range(1, len(lastRow))]
        nextRow = [1] + newRowMidPart + [1]
        return nextRow