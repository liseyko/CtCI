class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set(('a','e','i','o','u'))
        li, ri = 0, len(s)-1
        while li < ri:
            if s[li].lower() not in vowels:
                li += 1
            elif s[ri].lower() not in vowels:
                ri -= 1
            else:
                s[li], s[ri] = s[ri], s[li]
                li, ri = li + 1, ri - 1
        return ''.join(s)
