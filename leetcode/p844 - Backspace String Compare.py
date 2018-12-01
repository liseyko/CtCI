class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i, j = len(S) - 1, len(T) - 1
        
        while True:
            bs = 0
            while i >= 0 and (S[i] == '#' or bs > 0): 
                if S[i] == '#': bs += 1
                else: bs -= 1
                i -= 1
            while j >= 0 and (T[j] == '#' or bs > 0): 
                if T[j] == '#': bs += 1
                else: bs -= 1
                j -= 1
            if i < 0 and j < 0:
                return True
            elif i < 0 or j < 0:
                return False
            if S[i] != T[j]:
                return False
            i, j = i - 1, j - 1
