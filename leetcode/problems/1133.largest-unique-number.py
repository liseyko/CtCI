#
# @lc app=leetcode id=1133 lang=python3
#
# [1133] Largest Unique Number
#
# https://leetcode.com/problems/largest-unique-number/description/
#
# algorithms
# Easy (66.85%)
# Total Accepted:    5.4K
# Total Submissions: 8.1K
# Testcase Example:  '[5,7,3,9,4,9,8,3,1]'
#
# Given an array of integers A, return the largest integer that only occurs
# once.
# 
# If no integer occurs once, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: 
# The maximum integer in the array is 9 but it is repeated. The number 8 occurs
# only once, so it's the answer.
# 
# 
# Example 2:
# 
# 
# Input: [9,9,8,8]
# Output: -1
# Explanation: 
# There is no number that occurs only once.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 2000
# 0 <= A[i] <= 1000
# 
# 
#
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        
