class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        for i in range(k, len(nums)):
            heapq.heappushpop(h, nums[i])

        return heapq.heappop(h)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(s, e):
            pi = random.randint(s, e)
            nums[pi], nums[e] = nums[e], nums[pi]
            for i in range(s, e):
                if nums[i] < nums[e]:
                    nums[s], nums[i] = nums[i], nums[s]
                    s += 1
            nums[e], nums[s] = nums[s], nums[e]
            return s

        s, e, k = 0, len(nums)-1, len(nums)-k
        while True:
            pi = partition(s, e)
            if pi > k:
                e = pi-1
            elif pi < k:
                s = pi+1
            else:
                return nums[pi]
