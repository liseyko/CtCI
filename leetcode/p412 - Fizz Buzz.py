class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res, buf = [], []
        for i in range(1,n+1):
            if not i % 3: buf.append('Fizz')
            if not i % 5: buf.append('Buzz')
            if not buf: buf.append(str(i))
            res.append(''.join(buf))
            buf.clear()
        return res
    
    def fizzBuzz(self, n):
        res = ["" for i in range(1,n+1)]

        for i in range(2, n ,3):
            res[i] = 'Fizz'
        for i in range(4, n ,5):
            res[i] += 'Buzz'
        for i in range(0, n):
            if not res[i]: res[i] = str(i+1)
        return res
    
    def fizzBuzz(self, n):
        res, buf = [], []
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}

        for i in range(1,n+1):
            for key in fizz_buzz_dict.keys():
                if i % key == 0:
                    buf.append(fizz_buzz_dict[key])

            if not buf: buf = [str(i)]
            res.append(''.join(buf))
            buf.clear()

        return res