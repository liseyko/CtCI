class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w[::-1] for w in s.split()])

    def reverseWords(self, s: str) -> str:
        s = list(s)
        i = j = 0
        while i < len(s):
            if not s[i].isspace():
                j = i
                while j < len(s) and not s[j].isspace():
                    j += 1
                s[i:j] = s[i:j][::-1]
                i = j
            i += 1
        return ''.join(s)
