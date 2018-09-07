class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) > len(nums1):
            nums1, nums2, m, n = nums2, nums1, n, m

        while n > 0:
            if m > 0 and nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        print(nums1)



if __name__ == '__main__':
    s = Solution()
    s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    s.merge([2,0], 1, [1], 1)
    s.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)
    s.merge([1,2,3,4,6,0], 5, [5], 1)
