class Solution:

    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ai, bi = len(a), len(b)
        res = []
        while carry or ai or bi:
            if ai:
                carry, ai = carry + int(a[ai-1]), ai-1
            if bi:
                carry, bi = carry + int(b[bi-1]), bi-1
            res.append(str(carry % 2))
            carry //= 2
        return ''.join(res[::-1])

    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a

        result = [int(c) for c in a[::-1]] + [0]
        carry = 0

        for i in range(len(b)):
            carry, result[i] = divmod(result[i] + int(b[~i]) + carry, 2)
        i = len(b)
        while carry:
            carry, result[i] = divmod(result[i] + carry, 2)
            i += 1

        if not result[-1]:
            result.pop()

        return ''.join(map(str, result[::-1]))
