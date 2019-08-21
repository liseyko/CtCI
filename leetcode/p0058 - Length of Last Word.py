from itertools import *

class Solution(object):
    def lengthOfLastWord(self, s):
        return sum(1 for _ in takewhile(str.isalpha, dropwhile(str.isspace, imap(str, reversed(s)))))

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            r += 1
            i -= 1
        return r