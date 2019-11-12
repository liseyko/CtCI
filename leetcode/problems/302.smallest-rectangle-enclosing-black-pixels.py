#
# @lc app=leetcode id=302 lang=python3
#
# [302] Smallest Rectangle Enclosing Black Pixels
#
# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/
#
# algorithms
# Hard (50.22%)
# Total Accepted:    24.8K
# Total Submissions: 49.4K
# Testcase Example:  '[["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]]\n0\n2'
#
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a
# black pixel. The black pixels are connected, i.e., there is only one black
# region. Pixels are connected horizontally and vertically. Given the location
# (x, y) of one of the black pixels, return the area of the smallest
# (axis-aligned) rectangle that encloses all black pixels.
# 
# Example:
# 
# 
# Input:
# [
# ⁠ "0010",
# ⁠ "0110",
# ⁠ "0100"
# ]
# and x = 0, y = 2
# 
# Output: 6
# 
# 
#
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
