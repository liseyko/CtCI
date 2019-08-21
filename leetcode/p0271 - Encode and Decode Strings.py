class Codec:

    def encode(self, strs):
        return ''.join('%d:' % len(s) + s for s in strs)

    def decode(self, s):
        strs = []
        i, slen = 0, 0
        while i < len(s):
            if s[i] != ':':
                slen, i = slen * 10 + int(s[i]), i+1
                continue
            strs.append(s[i+1:i+1+slen])
            i += 1 + slen
            slen = 0

        return strs


class Codec:

    def encode(self, strs):
        return unichr(256).join(strs) if strs else unichr(257)

    def decode(self, s):
        return s.split(unichr(256)) if s != unichr(257) else []
