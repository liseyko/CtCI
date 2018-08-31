def findMedianSortedArrays(nums1, nums2):
    n, m = len(nums1), len(nums2)
    if n > m:
        nums1, nums2, n, m = nums2, nums1, m, n
    min_index, max_index = 0, n
      
    while (min_index <= max_index) :
        i = int((min_index + max_index) / 2)
        j = int(((n + m + 1) / 2) - i)
      
        if (i < n and j > 0 and nums2[j - 1] > nums1[i]) :
            min_index = i + 1
        elif (i > 0 and j < m and nums2[j] < nums1[i - 1]) :
            max_index = i - 1
        else:
            if (i == 0):
                median = nums2[j - 1]
            elif (j == 0):
                median = nums1[i - 1]
            else:
                median = max(nums1[i - 1], nums2[j - 1]) 
            break

    if ((n + m) % 2 == 1):
        return median
    if (i == n) :
        return ((median + nums2[j]) / 2.0)
    if (j == m) :
        return ((median + nums1[i]) / 2.0)
    return ((median + min(nums1[i], nums2[j])) / 2.0)



if __name__ == '__main__':
    nums = [1,3,5,7,9,11,13,15,17]
    xnums = [0,2,4,6,8,10,12,14,18]
    print(nums)
    print(xnums)
    print(findMedianSortedArrays([1], [2,3]))
    print(findMedianSortedArrays(nums, xnums))
    allnums = sorted(nums+xnums)
    print(allnums)
    print(allnums[len(allnums)//2])

    print(findMedianSortedArrays([1,3], [2,4,5]))

    print(findMedianSortedArrays([1,3], [2]))
    print(findMedianSortedArrays([], [1]))
    print(findMedianSortedArrays([1,1,1], [1,1,1]))
    print(findMedianSortedArrays([1,1,3,3], [1,1,3,3]))
