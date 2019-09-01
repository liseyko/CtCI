class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        self.total_cost = float('inf')
        def bt(h=0, csum = 0, pi=-1):
            if h == len(costs):
                self.total_cost = min(self.total_cost, csum)
                return
            for i in range(3):
                if i == pi:
                    continue
                bt(h+1, csum+costs[h][i], i)
        bt()
        return self.total_cost

    def minCost(self, costs: List[List[int]]) -> int:
        for i, cost in enumerate(costs[1:]):
            cost[0] += min(costs[i][1:])
            cost[1] += min(costs[i][0::2])
            cost[2] += min(costs[i][:-1])
        return min(costs[-1]) if costs else 0
