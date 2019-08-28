class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        def bt(buf=[], tiles=list(tiles)):
            if buf:
                res.add(''.join(buf))
            if not tiles:
                return
            for i, t in enumerate(tiles):
                bt(buf+[t], tiles[:i]+tiles[i+1:])
        bt()
        return len(res)

    def numTilePossibilities(self, tiles: str) -> int:
        td = collections.defaultdict(int)
        for c in tiles:
            td[c] += 1

        def bt(active_keys=set(td.keys())):
            n = 0
            for key in active_keys:
                n += 1
                td[key] -= 1
                n = n+bt(active_keys) if td[key] else n+bt(active_keys-{key})
                td[key] += 1
            return n

        return bt()
