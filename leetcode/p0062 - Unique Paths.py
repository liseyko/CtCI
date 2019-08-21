class Solution:
    """ dfs: slow, but with details 
    def uniquePaths(self, m, n):                
        self.paths = 0
        def dfs(i=0, j=0,path=[]):
            #print(i,j)
            if i==m-1 and j==n-1:
                #paths.append(path)
                self.paths += 1
            else:
                if i < m:
                    dfs(i+1, j) #, path+[(i+1,j)])
                if j < n:
                    dfs(i, j+1) #, path+[(i,j+1)])
                
        dfs()
        return self.paths
    """
    """
    def __init__(self):
        self.paths = [[0 for _ in range(100)] for _ in range(100)]
        for i in range(100):
            self.paths[0][i] = 1
            self.paths[i][0] = 1

        m = n = 100
        for i in range(1, m):
            for j in range(1, n):
                self.paths[i][j] = self.paths[i-1][j] + self.paths[i][j-1]
    """        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n > m: m, n = n, m
        self.paths = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            self.paths[0][i] = 1
            self.paths[i][0] = 1
        for i in range(n, m):
            self.paths[i][0] = 1

        
        for i in range(1, m):
            for j in range(1, n):
                self.paths[i][j] = self.paths[i-1][j] + self.paths[i][j-1]
        
        return self.paths[m-1][n-1]