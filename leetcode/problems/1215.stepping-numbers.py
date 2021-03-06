#
# @lc app=leetcode id=1215 lang=python3
#
# [1215] Stepping Numbers
#
# https://leetcode.com/problems/stepping-numbers/description/
#
# algorithms
# Medium (36.21%)
# Total Accepted:    2.9K
# Total Submissions: 7.9K
# Testcase Example:  '0\n21'
#
# A Stepping Number is an integer such that all of its adjacent digits have an
# absolute difference of exactly 1. For example, 321 is a Stepping Number while
# 421 is not.
# 
# Given two integers low and high, find and return a sorted list of all the
# Stepping Numbers in the range [low, high] inclusive.
# 
# 
# Example 1:
# Input: low = 0, high = 21
# Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]
# 
# 
# Constraints:
# 
# 
# 0 <= low <= high <= 2 * 10^9
# 
# 
#
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        
