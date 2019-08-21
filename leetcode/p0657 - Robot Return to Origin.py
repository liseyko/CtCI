class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = {'U':(1,0), 'D': (-1,0), 'R': (0,1), 'L': (0,-1)}
        pos = [0,0]
        for m in moves:
            pos = list(map(sum,zip(pos,d[m])))
            
        return pos == [0,0]

    def judgeCircle(self, moves):
        d = {'U': 0, 'D': 0, 'R': 0, 'L': 0}
        for m in moves:
            d[m] += 1
        
        return not d['U'] - d['D'] and not d['L'] - d['R']

    def judgeCircle(self, moves):
        x = y = 0
        for m in moves:
            if m == 'U': y -= 1
            elif m == 'D': y += 1
            elif m == 'L': x -= 1
            elif m == 'R': x += 1

        return x == y == 0

    def judgeCircle(self, moves):
        u, d, l, r = map(moves.count, 'UDLR')
        return u==d and l==r