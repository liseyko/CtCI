class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        d = collections.defaultdict(int)
        res = []
        for n in nums1:
            d[n] += 1
        for n in nums2:
            if n in d:
                res.append(n)
                d[n] -= 1
                if not d[n]:
                    del d[n]
        return res