class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        buf, res = 0, []
        for s in strs:
            for c in s:
                res.extend([c, c])
            res.extend([1, 0])
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        strs, buf, i = [], [], 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                buf.append(s[i])
            else:
                strs.append(''.join(buf))
                buf = []
            i += 2
        return strs


class Codec:

    def encode(self, strs):
        return unichr(256).join(strs) if strs else unichr(257)

    def decode(self, s):
        return s.split(unichr(256)) if s != unichr(257) else []
