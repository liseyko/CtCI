class Solution:
    """ first bruteforce solution """
    def _isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if getattr(s, 'val', None) != getattr(t, 'val', None):
            return False
        return s == t or\
            self._isSameTree(s.left, t.left) and\
            self._isSameTree(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self._isSameTree(s, t) or s and\
            (self.isSubtree(s.left, t) or
             self.isSubtree(s.right, t))
