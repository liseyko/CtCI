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
