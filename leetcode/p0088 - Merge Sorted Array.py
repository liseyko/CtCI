class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while n:
            if m and nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            elif n:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        m, n = m - 1, n - 1
        while n >= 0:
            nums1[k] = max(nums1[m], nums2[n]) if m+1 else nums2[n]
            k -= 1
            if m+1 and nums1[m] >= nums2[n]:
                m -= 1
            else:
                n -= 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1i, n2i, n1tail = m-1, n-1, m+n-1
        while n2i > -1:
            n1 = nums1[n1i] if n1i >= 0 else float('-inf')
            n2 = nums2[n2i]
            nums1[n1tail] = max(n1, n2)
            n1tail -= 1
            if n1 > n2:
                n1i -= 1
            else:
                n2i -= 1
