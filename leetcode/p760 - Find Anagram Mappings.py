class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = collections.defaultdict(list)

        for i, c in enumerate(B):
            d[c].append(i)

        for i, c in enumerate(A):
            A[i] = d[c].pop()

        return A