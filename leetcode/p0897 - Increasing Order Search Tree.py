class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            root.left = None
            self.tail.right = root
            self.tail = self.tail.right
            dfs(root.right)

        new_root = self.tail = TreeNode('dummy')
        dfs(root)
        return new_root.right

    def increasingBST(self, root, nxt=None):
        if not root:
            return nxt
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, nxt)
        return res
