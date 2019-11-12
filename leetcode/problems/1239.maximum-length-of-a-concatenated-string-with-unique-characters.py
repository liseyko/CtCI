#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#
# algorithms
# Medium (41.24%)
# Total Accepted:    5.4K
# Total Submissions: 13.2K
# Testcase Example:  '["un","iq","ue"]'
#
# Given an array of strings arr. String s is a concatenation of a sub-sequence
# of arr which have unique characters.
# 
# Return the maximum possible length of s.
# 
# 
# Example 1:
# 
# 
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq" and
# "ique".
# Maximum length is 4.
# 
# 
# Example 2:
# 
# 
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
# 
# 
# Example 3:
# 
# 
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lower case English letters.
# 
# 
#
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
