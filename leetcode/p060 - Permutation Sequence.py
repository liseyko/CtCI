import math

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if not n: return ""
        r = []
        nums = [str(i) for i in range(1,n+1)]
        step = math.factorial(n-1)

        while nums:
            for i in nums:
                k -= step
                if k <= 0:
                    r.append(i)
                    nums.remove(i)
                    if k == 0:
                        r += nums[::-1]
                        return ''.join(r)
                    k, n = k + step, n - 1
                    step = step // n
                    break

    def getPermutation(self, n, k):
        elements = range(1, n+1)
        NN = reduce(operator.mul, elements) # n!
        k, result = (k-1) % NN, ''
        while len(elements) > 0:
            NN = NN / len(elements)
            i, k = k / NN, k % NN
            result += str(elements.pop(i))
        return result

    def getPermutation(self, n, k):
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation