class Solution:

    def simplifyPath(self, path):
        r = []
        for d in path.split('/'):
            if d == '..' and len(r) > 0:
                r.pop()
            if d not in ('','.','..'):
                r.append(d)

        return '/'+'/'.join(r)