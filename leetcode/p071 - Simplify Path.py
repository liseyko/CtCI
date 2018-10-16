class Solution:

    def simplifyPath(self, path):

        path = [x for x in path.split('/') if x not in ('','.')]
        i, j = 0, len(path) - 1

        while i <= j:
            if path[i] == '..':
                if i > 0:
                    del path[i - 1]
                    i, j = i - 1, j - 1
                del path[i]
                j -= 1
                continue
            i += 1

        return '/'+'/'.join(path)