#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence 
#
# https://leetcode.com/problems/shortest-common-supersequence/description/
#
# algorithms
# Hard (49.62%)
# Total Accepted:    5.7K
# Total Submissions: 11.4K
# Testcase Example:  '"abac"\n"cab"'
#
# Given two strings str1 and str2, return the shortest string that has both
# str1 and str2 as subsequences.  If multiple answers exist, you may return any
# of them.
# 
# (A string S is a subsequence of string T if deleting some number of
# characters from T (possibly 0, and the characters are chosen anywhere from T)
# results in the string S.)
# 
# 
# 
# Example 1:
# 
# 
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation: 
# str1 = "abac" is a subsequence of "cabac" because we can delete the first
# "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these
# properties.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.
# 
# 
#
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
