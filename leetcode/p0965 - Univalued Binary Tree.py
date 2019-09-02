class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left and root.left.val != root.val or\
           root.right and root.right.val != root.val:
            return False
        return self.isUnivalTree(root.left) and\
            self.isUnivalTree(root.right)
