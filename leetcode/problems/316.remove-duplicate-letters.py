#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (33.74%)
# Total Accepted:    65.4K
# Total Submissions: 193.7K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appears once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
# 
# Example 1:
# 
# 
# Input: "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: "cbacdcbc"
# Output: "acdb"
# 
# 
#
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
