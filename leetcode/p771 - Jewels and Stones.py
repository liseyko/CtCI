class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        #return len([x for x in S if x in J])
        return sum(x in J for x in S)