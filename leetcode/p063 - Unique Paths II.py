class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid: return 0
        n, m = len(obstacleGrid[0]), len(obstacleGrid)
        self.paths = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            if not obstacleGrid[0][i]: self.paths[0][i] = 1
            else: break
        for j in range(m):
            if not obstacleGrid[j][0]: self.paths[j][0] = 1
            else: break
                
        for j in range(1, m):
            for i in range(1, n):
                if obstacleGrid[j][i]: continue
                else:
                    self.paths[j][i] = self.paths[j-1][i] + self.paths[j][i-1]

        return self.paths[-1][-1]

    def uniquePathsWithObstacles(self, paths):
        if not paths or paths[0][0]: return 0
        n, m, paths[0][0] = len(paths[0]), len(paths), 1

        for i in range(1,n):
            paths[0][i] = int(not paths[0][i] and paths[0][i-1])

        for j in range(1,m):
            paths[j][0] = int(not paths[j][0] and paths[j-1][0])

        for j in range(1, m):
            for i in range(1, n):
                if paths[j][i]: paths[j][i] = 0
                else:
                    paths[j][i] = paths[j-1][i] + paths[j][i-1]

        return paths[-1][-1]