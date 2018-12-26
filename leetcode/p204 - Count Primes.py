class Solution:
    
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i]:
                s[i * i:n:i] = [0] * len(s[i * i:n:i])
        return sum(s)    
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [False, False] + [True] * (n-2)
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                #print(primes[i * i:n:i])
                for j in range(i*i,len(primes),i):
                    primes[j] = 0
                #primes[i * 2:n:i] = [0] * len(primes[i * 2:n:i])
        #print(primes)
        return sum(primes)
