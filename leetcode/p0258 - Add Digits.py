class Solution:
    # If an integer is like 100a+10b+c, then (100a+10b+c)%9=(a+99a+b+9b+c)%9=(a+b+c)%9
    def addDigits(self, num):    
        if not num: return 0
        return num % 9 or 9
    
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num > 9:
            return self.addDigits(sum([int(i) for i in str(num)]))
        return num
    
    def addDigits(self, num):
        while num > 9:
            num = sum([int(i) for i in str(num)])
        return num

    def addDigits(self, num):
        while num > 9:
            tmp = 0
            while num:
                tmp += num % 10
                num //= 10
            num = tmp
        return num