class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = r = 0
        i, res = 0, 0
        while i < len(gas):
            r += gas[i] - cost[i]
            if r < 0:
                l += r
                r, res = 0, i + 1
            i += 1
        if l + r < 0:
            return -1
        return res