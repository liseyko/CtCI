class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort();  nums2.sort()
        i = j = 0;  m, n = len(nums1), len(nums2)
        res = [None]
        
        while i < m and j < n:
            if nums1[i] < nums2[j]: i += 1
            elif nums1[i] > nums2[j]: j += 1
            else:
                if nums1[i] != res[-1]:
                    res.append(nums1[i])
                i, j = i + 1, j + 1
        return res[1:]

