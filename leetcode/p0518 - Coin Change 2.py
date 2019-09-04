class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        sumsq = [1]+[0]*(amount)

        for c in coins:
            for i in range(len(sumsq)):
                if c > i:
                    continue
                sumsq[i] += sumsq[i-c]
            #print(sumsq)
        return sumsq[-1]
