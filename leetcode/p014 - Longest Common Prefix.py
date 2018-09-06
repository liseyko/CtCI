class Solution(object):

    def longestCommonPrefix(self, strs):
        if not strs or not strs[0]:
            return ""
        i = -1
        while True:
            i += 1
            if i < len(strs[0]):
                c =  strs[0][i]
            for s in strs:
                if i == len(s) or c != s[i]:
                    return s[0:i]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['abcd','abce','abec']))
    print(s.longestCommonPrefix(['abcd','abce','']))
    print(s.longestCommonPrefix(['abcd','abce','f']))
    print(s.longestCommonPrefix(['abcde','abcev','fbcde']))
