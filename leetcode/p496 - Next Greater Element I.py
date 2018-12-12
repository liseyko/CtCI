class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2: return []
        
        d = {nums2[-1]: -1}
        for i in range(len(nums2)-2,-1,-1):
            n = nums2[i]
            nxt = i+1
            while nxt != -1 and nums2[nxt] <= n:
                nxt = d[nums2[nxt]]
            d[n] = nxt
        #print(d)
        nums2.append(-1)
        return [nums2[d[i]] for i in nums1]