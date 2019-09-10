class Solution:
    def __init__(self):
        self.vals = set()

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        if (k - root.val) in self.vals:
            return True
        self.vals.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
