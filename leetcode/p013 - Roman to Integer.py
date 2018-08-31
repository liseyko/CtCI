class Solution:
    def __init__(self):
        self.r2i = { 'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        self.rr2i = { 'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900 }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
        """
        sum, i = 0, len(s)-1
        while i > 0:
            if s[i-1:i+1] in self.rr2i:
                sum += self.rr2i[s[i-1:i+1]]
                i-=2
            else:
                sum += self.r2i[s[i]]
                print(i, self.r2i[s[i]])
                i-=1

        if len(s) == 1 or (len(s) > 1 and s[0:1+1] not in self.rr2i):
            sum += self.r2i[s[0]]
        return sum


if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("MCMXCIV"))
    print(sol.romanToInt("III"))
    print(sol.romanToInt("LVIII"))
    print(sol.romanToInt("IX"))
    print(sol.romanToInt("IM"))