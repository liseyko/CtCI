class Solution(object):
    def reverseWords_inplace(self, s, delimeter=' '):
        if len(s) == 0 or s.isspace():
            return ""

        s = list(s)

        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]

        i, j = 0, 0
        while j < len(s)-1:
            while j < len(s)-1 and s[j] == delimeter:
                j += 1
            l = j  # reversed word end marker
            while j < len(s)-1 and s[j+1] != delimeter:
                j += 1
            r = j  # reversed word start marker

            for k in range((r-l+1)//2):  # reverse each word back again
                s[l+k], s[r-k] = s[r-k], s[l+k]

            if i != l:  # if it's not in place already, shift it left
                for k in range(r-l+1):
                    s[i+k] = s[l+k]

            if r - l > 0:  # postprocessing: update pointers
                i = i + r - l
                if j < len(s)-1:
                    s[i+1] = delimeter
                    i += 2
                    j += 1
        while s[i] == delimeter:
            i -= 1
        return ''.join(s[:i+1])

    def reverseWords(self, s, delimeter=' '):
        """
        :type s: str
        :rtype: str
        """
        l, r = 0, len(s)-1
        while l <= r and s[l] == delimeter:
            l += 1
        while r >= l and s[r] == delimeter:
            r -= 1
        if r < l:
            return ""

        result = []
        i, j = r, r+1
        while i > l:
            if s[i] == delimeter:  # delimeter
                result.append(s[i+1:j] + delimeter)
                while s[i-1] == delimeter:
                    i -= 1
                j = i
            i -= 1
        result.append(s[i:j])
        return ''.join(result)

    def reverseWords(self, s):
        return ' '.join(w for w in s.split()[::-1])

    def reverseWords(self, s, delimeters={' '}):
        r, i = [], len(s)-1
        while i > -1:
            if s[i] == ' ':
                i -= 1
            else:
                wl = 0
                while i > -1 and s[i] != ' ':
                    wl, i = wl + 1, i - 1
                r.append(s[i+1:i+wl+1])
        return ' '.join(r)

    def reverseWords(self, s, delimiter=' '):

        def trim(s, delimeter=' '):
            i = j = 0
            n = len(s)
            while j < n:
                while j < n and s[j] == delimeter:
                    j += 1
                while j < n and s[j] != delimeter:
                    s[i] = s[j]
                    i, j = i+1, j+1
                while j < n and s[j] == delimeter:
                    j += 1
                if j < n:
                    s[i] = delimeter
                    i += 1
            s[i:] = []

        def reverse(s, i=0, j=None):
            if j is None:
                j = len(s)-1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1

        s = list(s)
        trim(s)
        reverse(s)
        i = j = 0
        while j < len(s):
            j += 1
            if j == len(s) or s[j] == delimiter:
                reverse(s, i, j-1)
                i = j+1

        return ''.join(s)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("  the sky is    blue   "))
    print(s.reverseWords_inplace("  the sky is    blue   "))
    print(s.reverseWords_inplace(""))
    print(s.reverseWords_inplace("the sky is blue"))
    print(s.reverseWords_inplace("     "))
