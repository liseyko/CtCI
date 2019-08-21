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

    def compress(self, chars: List[str]) -> int:
        r = w = 0
        while r < len(chars):
            cnt = 1
            while r < len(chars)-1 and chars[r] == chars[r+1]:
                r, cnt = r+1, cnt+1
            chars[w] = chars[r]
            r, w = r+1, w+1
            if cnt > 1:
                for c in str(cnt):
                    chars[w] = c
                    w += 1
        return w

    def compress(self, chars: List[str]) -> int:
        r = w = 0

        def countDupes(r):
            cnt = 1
            while r < len(chars)-1 and chars[r] == chars[r+1]:
                r, cnt = r+1, cnt+1
            return cnt, r

        def compress1char(r, w, cnt):
            chars[w], w = chars[r], w+1
            if cnt > 1:
                for c in str(cnt):
                    chars[w] = c
                    w += 1
            return w

        while r < len(chars):
            cnt, r = countDupes(r)
            w = compress1char(r, w, cnt)
            r += 1
        return w
