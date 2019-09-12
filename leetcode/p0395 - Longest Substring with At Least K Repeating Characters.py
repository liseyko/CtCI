class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

    def longestSubstring(self, s, k):
        cnts = collections.Counter(s)
        for c, cnt in cnts.items():
            if cnt < k:
                return max([self.longestSubstring(substr, k)
                            for substr in s.split(c) if len(substr)>=k] or [0])
        return len(s)
