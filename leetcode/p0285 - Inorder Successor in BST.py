class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            curNode = stack[-1]
            if curNode.val > p.val:
                return curNode
            root = stack.pop().right

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        def dfs_find(root=root, n=p):
            if not root:
                return
            dfs_find(root.left)
            if self.res:
                return
            if root == n:
                self.found = True
            elif self.found:
                self.res = root
                return
            dfs_find(root.right)

        self.found = False
        self.res = None
        dfs_find()
        return self.res
