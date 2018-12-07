class Solution:
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get)    
    
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.defaultdict(int)
        
        for n in nums:
            d[n] += 1
            
        return [k for k, v in sorted([i for i in d.items()], key = lambda x: x[1], reverse = True)[:k]]