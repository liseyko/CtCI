class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
    # @return a list of integers
    '''
    from up to down, then left to right
    
    0   1   11  110
            10  111
                101
                100
                
    start:      [0]
    i = 0:      [0, 1]
    i = 1:      [0, 1, 3, 2]
    i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
    '''
    def grayCode(self, n):
        res = [0]
        for i in range(n):
            res += [x|(1<<i) for x in res[::-1]]
        return res
    
    def grayCode(self, n):
        res = [0]
        for i in range(n):
            res += [x + pow(2, i) for x in reversed(res)]
        return res