class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return 1+max([0]+[self.maxDepth(c) for c in root.children])
