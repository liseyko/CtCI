class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mirror = ['0','1','','','','','9','','8','6']
        i, j = 0, len(num)-1
        while i <= j:
            if num[i] != mirror[int(num[j])]:
                return False
            i, j = i+1, j-1
        return True
