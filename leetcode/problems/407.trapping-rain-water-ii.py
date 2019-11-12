#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#
# https://leetcode.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (40.22%)
# Total Accepted:    32.5K
# Total Submissions: 80.8K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# Given an m x n matrix of positive integers representing the height of each
# unit cell in a 2D elevation map, compute the volume of water it is able to
# trap after raining.
# 
# 
# 
# Note:
# 
# Both m and n are less than 110. The height of each unit cell is greater than
# 0 and is less than 20,000.
# 
# 
# 
# Example:
# 
# 
# Given the following 3x6 height map:
# [
# ⁠ [1,4,3,1,3,2],
# ⁠ [3,2,1,3,2,4],
# ⁠ [2,3,3,2,3,1]
# ]
# 
# Return 4.
# 
# 
# 
# 
# The above image represents the elevation map
# [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
# 
# 
# 
# 
# 
# After the rain, water is trapped between the blocks. The total volume of
# water trapped is 4.
# 
#
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
