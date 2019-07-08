import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        for i in range(k, len(nums)):
            heapq.heappushpop(h, nums[i])

        return heapq.heappop(h)        

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest(self, nums, k):
        random.shuffle(nums)
        print(nums, k)
        return self.quickselect(nums, -k)

    def quickselect(self, l, k, pivot_fn=random.choice):
        """
        Select the kth element in l (0 based)
        :param l: List of numerics
        :param k: Index
        :param pivot_fn: Function to choose a pivot, defaults to random.choice
        :return: The kth element of l
        """
        if k < 0:
            k += len(l)

        if len(l) == 1:
            assert k == 0
            return l[0]

        pivot = pivot_fn(l)

        lows = [el for el in l if el < pivot]
        highs = [el for el in l if el > pivot]
        pivots = [el for el in l if el == pivot]

        if k < len(lows):
            return self.quickselect(lows, k, pivot_fn)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return self.quickselect(highs, k-len(lows)-len(pivots), pivot_fn)
