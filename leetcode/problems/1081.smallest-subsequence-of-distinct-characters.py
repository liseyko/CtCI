#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (44.82%)
# Total Accepted:    5.7K
# Total Submissions: 12.7K
# Testcase Example:  '"cdadabcc"'
#
# Return the lexicographically smallest subsequence of text that contains all
# the distinct characters of text exactly once.
# 
# 
# 
# Example 1:
# 
# 
# Input: "cdadabcc"
# Output: "adbc"
# 
# 
# 
# Example 2:
# 
# 
# Input: "abcd"
# Output: "abcd"
# 
# 
# 
# Example 3:
# 
# 
# Input: "ecbacba"
# Output: "eacb"
# 
# 
# 
# Example 4:
# 
# 
# Input: "leetcode"
# Output: "letcod"
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= text.length <= 1000
# text consists of lowercase English letters.
# 
# 
# 
# 
# 
# 
#
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        
