class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        a = [0]*60
        for t in time:
            res += a[(60 - t % 60) % 60]
            a[t % 60] += 1
        return res

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        d = collections.defaultdict(int)
        for t in time:
            matchingPair = (60 - t % 60) % 60
            res += d[matchingPair]
            d[t % 60] += 1
        return res
