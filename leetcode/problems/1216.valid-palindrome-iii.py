#
# @lc app=leetcode id=1216 lang=python3
#
# [1216] Valid Palindrome III
#
# https://leetcode.com/problems/valid-palindrome-iii/description/
#
# algorithms
# Hard (42.23%)
# Total Accepted:    3K
# Total Submissions: 7.2K
# Testcase Example:  '"abcdeca"\n2'
#
# Given a string s and an integer k, find out if the given string is a
# K-Palindrome or not.
# 
# A string is K-Palindrome if it can be transformed into a palindrome by
# removing at most k characters from it.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcdeca", k = 2
# Output: true
# Explanation: Remove 'b' and 'e' characters.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s has only lowercase English letters.
# 1 <= k <= s.length
# 
# 
#
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
