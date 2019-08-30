class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_root = self.tail = TreeNode('dummy')

        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            self.tail.right = root
            self.tail = self.tail.right
            self.tail.left = None
            rc, self.tail.right = self.tail.right, None
            dfs(rc)

        dfs(root)
        return new_root.right
