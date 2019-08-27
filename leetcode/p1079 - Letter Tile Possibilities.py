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
