class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            buf = []
            if i%3 == 0:
                buf += ['Fizz']
            if i%5 == 0:
                buf += ['Buzz']
            if not buf:
                buf = str(i)
            res.append(''.join(buf))
        return res
