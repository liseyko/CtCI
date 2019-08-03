class Solution(object):
    def compress(self, chars):
        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while (i + 1) < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left


class Solution:
    def compress(self, chars: List[str]) -> int:
        wptr, cnt = 0, 1

        def flushCnt():
            nonlocal wptr, cnt
            wptr += 1
            if cnt == 1:
                return
            for c in str(cnt):
                chars[wptr] = c
                wptr += 1
            cnt = 1

        for rptr in range(len(chars)):
            if rptr < len(chars)-1 and chars[rptr] == chars[rptr+1]:
                cnt += 1
            else:
                flushCnt()
                if wptr < rptr+1 < len(chars):
                    chars[wptr] = chars[rptr+1]

        return wptr
