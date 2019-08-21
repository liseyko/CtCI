class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res, buf = [], []
        for i in range(1, n+1):
            if not i % 3:
                buf.append('Fizz')
            if not i % 5:
                buf.append('Buzz')
            if not buf:
                buf.append(str(i))
            res.append(''.join(buf))
            buf.clear()
        return res

    def fizzBuzz(self, n):
        res = ["" for i in range(n+1)]
        for i in range(1, n+1):
            if not i % 3:
                res[i] = "Fizz"
            if not i % 5:
                res[i] += "Buzz"
            if not res[i]:
                res[i] = str(i)
        return res[1:]

    def fizzBuzz(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5)
                or str(i) for i in range(1, n+1)]
