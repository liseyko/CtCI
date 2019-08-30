class Solution:
    def fib(self, N: int) -> int:
        data = [0, 1]
        for _ in range(2, N+1):
            data.append(sum(data[-2:]))
        return data[N]

class Solution:
    def fib(self, N: int) -> int:
        nums = collections.deque([0, 1]) if N else [0]
        for _ in range(2, N+1):
            nums.append(nums.popleft() + nums[-1])
        return nums[-1]


class Solution:
    """ Recursive """
    def _fib(self, N):
        if self.nums[N] is None:
            self.nums[N] = self._fib(N-2) + self._fib(N-1)
        return self.nums[N]

    def fib(self, N: int) -> int:
        self.nums = [0, 1] + [None for _ in range(2, N+1)]
        return self._fib(N)
