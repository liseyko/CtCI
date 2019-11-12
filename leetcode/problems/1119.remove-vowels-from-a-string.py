#
# @lc app=leetcode id=1119 lang=python3
#
# [1119] Remove Vowels from a String
#
# https://leetcode.com/problems/remove-vowels-from-a-string/description/
#
# algorithms
# Easy (87.85%)
# Total Accepted:    15.3K
# Total Submissions: 17.4K
# Testcase Example:  '"leetcodeisacommunityforcoders"'
#
# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and
# return the new string.
# 
# 
# 
# Example 1:
# 
# 
# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# 
# 
# Example 2:
# 
# 
# Input: "aeiou"
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# S consists of lowercase English letters only.
# 1 <= S.length <= 1000
# 
# 
#
class Solution:
    def removeVowels(self, S: str) -> str:
        
