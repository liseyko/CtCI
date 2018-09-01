class Solution(object):
    def reverseWords_inplace(self, s, delimeter = ' '):
        if len(s) == 0 or s.isspace():
            return ""

        s = list(s)

        for i in range(len(s)//2):
            s[i],s[~i] = s[~i],s[i]

        i, j = 0, 0
        while j < len(s)-1:
            while j < len(s)-1 and s[j] == delimeter:
                j += 1
            l = j # reversed word end marker
            while j < len(s)-1 and s[j+1] != delimeter:
                j += 1
            r = j # reversed word start marker
            #print(l,r)
            #print(s)

            for k in range((r-l+1)//2): # reverse each word back again
                s[l+k], s[r-k] = s[r-k], s[l+k]

            if i != l: # if it's not in place already, shift it left
                for k in range(r-l+1):
                    s[i+k] = s[l+k]

            if r-l > 0: # postprocessing: update pointers
                i = i + r - l
                if j < len(s)-1:
                    s[i+1] = delimeter
                    i += 2
                    j += 1
        while s[i] == delimeter:
            i -= 1
        return s[:i+1]
        #return ''.join(s[:i+1])


    def reverseWords(self, s, delimeter = ' '):
        """
        :type s: str
        :rtype: str
        """
        l, r = 0, len(s)-1
        while l <= r and s[l] == delimeter: l += 1
        while r >= l and s[r] == delimeter: r -= 1
        if r < l:
            return ""

        result = []
        i, j = r, r+1
        #for i in range(r, l-1, -1):
        while i > l:
            if s[i] == delimeter:  # delimeter
                result.append(s[i+1:j] + delimeter)
                while s[i-1] == delimeter: 
                    i -= 1
                j = i
            i -= 1
        result.append(s[i:j])
        return ''.join(result)      

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("  the sky is    blue   "))
    print(s.reverseWords_inplace("  the sky is    blue   "))
    print(s.reverseWords_inplace(""))
    print(s.reverseWords_inplace("the sky is blue"))
    print(s.reverseWords_inplace("     "))
    """
    print('[',s.reverseWords(""),']',sep='')
    print('[',s.reverseWords(" "),']',sep='')
    print('[',s.reverseWords("        "),']',sep='')
    """