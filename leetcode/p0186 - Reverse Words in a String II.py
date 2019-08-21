class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def rev(i, j):
            while i < j:
                str[i], str[j] = str[j], str[i]
                i, j = i + 1, j - 1
        i, ls = 0, len(str)
        for j in range(ls+1):
            if j == ls or str[j] == ' ':
                rev(i, j-1)
                i = j + 1

        rev(0, ls-1)

    def reverseWords(self, str):
        def rev(i, j):
            while i < j:
                str[i], str[j] = str[j], str[i]
                i, j = i + 1, j - 1

        i, ls = 0, len(str)
        for j in range(ls+1):
            if j == ls or str[j] == ' ':
                rev(i, j-1)
                i = j + 1

        str.reverse()
