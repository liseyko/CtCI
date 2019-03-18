class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        return (1 - K % 2) ^ self.kthGrammar(N-1, (K+1)//2)

    def kthGrammar(self, N, K):
        if N == 1:
            return 0
        if K <= (2**(N-2)):
            return self.kthGrammar(N-1, K)
        return self.kthGrammar(N-1, K - 2**(N-2)) ^ 1

    def kthGrammar(self, N, K):
        return bin(K - 1).count('1') % 2
