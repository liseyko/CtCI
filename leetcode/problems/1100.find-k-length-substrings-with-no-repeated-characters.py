#
# @lc app=leetcode id=1100 lang=python3
#
# [1100] Find K-Length Substrings With No Repeated Characters
#
# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/description/
#
# algorithms
# Medium (71.25%)
# Total Accepted:    4.4K
# Total Submissions: 6.2K
# Testcase Example:  '"havefunonleetcode"\n5'
#
# Given a string S, return the number of substrings of length K with no
# repeated characters.
# 
# 
# 
# Example 1:
# 
# 
# Input: S = "havefunonleetcode", K = 5
# Output: 6
# Explanation: 
# There are 6 substrings they are :
# 'havef','avefu','vefun','efuno','etcod','tcode'.
# 
# 
# Example 2:
# 
# 
# Input: S = "home", K = 5
# Output: 0
# Explanation: 
# Notice K can be larger than the length of S. In this case is not possible to
# find any substring.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 10^4
# All characters of S are lowercase English letters.
# 1 <= K <= 10^4
# 
# 
#
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        
