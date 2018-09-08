class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s0, s1 = ['1'], []
        for _ in range(1,n):
            c0, c_cnt = s0[0], 0
            for c1 in s0:
                if c1 != c0:
                    s1.extend([str(c_cnt),c0])
                    c0, c_cnt = c1, 1
                else:
                    c_cnt += 1
            s1.extend([str(c_cnt),c0])
            s0, s1 = s1, []
        return ''.join(s0)