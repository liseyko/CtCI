class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        n, m = len(matrix[0])-1, len(matrix)-1
        self.t = target

        def bs(l=0, r=m, y=None):
            if y is None:
                y = (r - l) // 2 + l
                if r-l <= 0:
                    if matrix[y][0] > self.t:
                        return False
                    elif matrix[y][0] == self.t:
                        return True
                    else:
                        if self.t > matrix[y][n]:
                            return False
                        return bs(0, n,  y)
                else:
                    if matrix[y][0] > self.t:
                        return bs(l, y-1)
                    elif matrix[y+1][0] > self.t:
                        if self.t > matrix[y][n]:
                            return False
                        return bs(0, n,  y)
                    else:
                        return bs(y+1, r)
            else:
                x = (r - l) // 2 + l
                if r-l <= 0:
                    if matrix[y][x] == self.t:
                        return True
                    else:
                        return False
                else:
                    if matrix[y][x] > self.t:
                        return bs(l, x-1, y)
                    elif matrix[y][x] < self.t:
                        return bs(x+1, r, y)
                    else:
                        return True
        return bs()
