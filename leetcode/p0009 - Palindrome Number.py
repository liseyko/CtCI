class Solution:
    def isPalindrome(self, x: int) -> bool:
        rx = 0
        cx = x if x > 0 else None
        while cx:
            rx = rx * 10 + cx % 10
            cx //= 10
        return x == rx
