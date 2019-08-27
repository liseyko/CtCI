class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def bt(buf=[], tiles = list(tiles)):
            if buf:
                res.add(''.join(buf))
            if not tiles:
                return
            for i, t in enumerate(tiles):
                bt(buf+[t], tiles[:i]+tiles[i+1:])
        bt()
        return len(res)

    def numTilePossibilities(self, tiles: str) -> int:
        t = collections.defaultdict(int)
        for c in tiles:
            t[c] += 1
        res = -1
        def bt():
            nonlocal res
            res += 1
            for key in t:
                if t[key]:
                    t[key] -= 1
                    bt()
                    t[key] += 1
        bt()
        return res