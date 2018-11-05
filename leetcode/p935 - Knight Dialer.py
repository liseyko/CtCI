class Solution:
    def __init__(self):
        self.moves = {0: [4,6], 1: [6,8], 2: [7,9], 3: [4,8], 4: [0,3,9], 6: [0,1,7], 7: [2,6], 8: [1,3], 9: [2,4]}
        #self.r = {1: [1 for _ in range(10)]}
        self.res = [1 for _ in range(10)]

    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        def dp(i):
            self.r[i] = [0 for _ in range(10)]
            for num in self.moves.keys():
                for move in self.moves[num]:
                    self.r[i][move] = (self.r[i][move] + self.r[i-1][num]) % (10**9 + 7)
        
        #if N <= len(self.r):
        #    return sum(self.r[N]) % (10**9 + 7)
        
        #for i in range(len(self.r)+1, N+1):
        #    dp(i)
        if N == 1: return 10
        
        for _ in range(N-1):
            next_res = [0 for _ in range(10)]
            for num in self.moves.keys():
                for move in self.moves[num]:
                    next_res[move] = (next_res[move] + self.res[num]) % (10**9 + 7)
            self.res = next_res
            
        return sum(self.res) % (10**9 + 7)
        #print(self.r) 
        
        #return sum(self.r[N]) % (10**9 + 7)

    def knightDialer(self, N):
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in xrange(N-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD