class RHash():
    def __init__(self, s):
        self.d = 256
        self.q = 101
        self.h = pow(self.d, len(s)-1, self.q)
        self.val = 0
        for c in s:
            self.append(c)

    def append(self, c):
        self.val = (self.val * self.d + ord(c)) % self.q

    def rmleft(self, c):
        self.val = (self.val - self.h * ord(c) + self.q) % self.q

    def __eq__(self, other):
        return self.val == other.val


class Solution:
    """ Rabin-Karp """
    def strStr(self, haystack, needle):
        hl, nl = len(haystack), len(needle)
        if not needle:
            return 0
        if not haystack or nl > hl:
            return -1

        nh, hh = RHash(needle), RHash(haystack[:nl])
        if nh == hh and haystack[:nl] == needle:
            return 0

        for i in range(nl, hl):
            hh.rmleft(haystack[i-nl])
            hh.append(haystack[i])
            if hh == nh and haystack[i-nl+1:i+1] == needle:
                return i-nl+1
        return -1


class Solution:
    """ KMP """
    def prefixTable(self, pattern):
        pt = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = pt[j-1]
            if pattern[i] == pattern[j]:
                j += 1
            pt[i] = j
        return pt

    def strStr(self, haystack, needle):
        if not needle or len(needle) == len(haystack) \
           and needle == haystack:
            return 0
        if len(needle) < len(haystack):
            pt = self.prefixTable(needle)
            j = 0
            for i in range(len(haystack)):
                while j > 0 and haystack[i] != needle[j]:
                    j = pt[j-1]
                if haystack[i] == needle[j]:
                    j += 1
                if j == len(needle):
                    return i - j + 1
        return -1
