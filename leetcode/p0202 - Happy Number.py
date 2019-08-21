class Solution(object):
    def isHappy(self, n):
        mem = set()
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in mem:
                return False
            else:
                mem.add(n)

        return True

    def isHappy(self, n: int) -> bool:
        hist = set()
        while n != 1:
            if n in hist:
                return False
            hist.add(n)
            k = 0
            while n:
                k += (n % 10)**2
                n //= 10
            n = k
        return True
