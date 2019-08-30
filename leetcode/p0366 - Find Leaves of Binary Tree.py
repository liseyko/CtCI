class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.res = []
        while root and not self._isLeaf(root):
            self.res.append([])
            self._findAndPluckLeaves(root)
        return self.res + [[root.val]] if root else self.res

    def _isLeaf(self, root):
        return root and not root.left and not root.right

    def _findAndPluckLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        for child in ('left', 'right'):
            if self._isLeaf(getattr(root, child)):
                self.res[-1].append(getattr(root, child).val)
                setattr(root, child, None)
            else:
                self._findAndPluckLeaves(getattr(root, child))
