#
# @lc app=leetcode id=288 lang=python3
#
# [288] Unique Word Abbreviation
#
# https://leetcode.com/problems/unique-word-abbreviation/description/
#
# algorithms
# Medium (20.81%)
# Total Accepted:    45.7K
# Total Submissions: 219.7K
# Testcase Example:  '["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]\n' +
  '[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]'
#
# An abbreviation of a word follows the form <first letter><number><last
# letter>. Below are some examples of word abbreviations:
# 
# 
# a) it                      --> it    (no abbreviation)
# 
# ⁠    1
# ⁠    ↓
# b) d|o|g                   --> d1g
# 
# ⁠             1    1  1
# ⁠    1---5----0----5--8
# ⁠    ↓   ↓    ↓    ↓  ↓    
# c) i|nternationalizatio|n  --> i18n
# 
# ⁠             1
# ⁠    1---5----0
# ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
# 
# 
# Assume you have a dictionary and given a word, find whether its abbreviation
# is unique in the dictionary. A word's abbreviation is unique if no other word
# from the dictionary has the same abbreviation.
# 
# Example:
# 
# 
# Given dictionary = [ "deer", "door", "cake", "card" ]
# 
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true
# 
# 
#
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        

    def isUnique(self, word: str) -> bool:
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
