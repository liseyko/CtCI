#
# @lc app=leetcode id=564 lang=python3
#
# [564] Find the Closest Palindrome
#
# https://leetcode.com/problems/find-the-closest-palindrome/description/
#
# algorithms
# Hard (19.17%)
# Total Accepted:    16.6K
# Total Submissions: 86.6K
# Testcase Example:  '"1"'
#
# Given an integer n, find the closest integer (not including itself), which is
# a palindrome. 
# 
# The 'closest' is defined as absolute difference minimized between two
# integers.
# 
# Example 1:
# 
# Input: "123"
# Output: "121"
# 
# 
# 
# Note:
# 
# The input n is a positive integer represented by string, whose length will
# not exceed 18.
# If there is a tie, return the smaller one as answer.
# 
# 
#
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
