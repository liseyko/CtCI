class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(n=root):
            if not n or not self.cntr:
                return
            dfs(n.left)
            self.cntr -= 1
            if not self.cntr:
                self.res = n.val
            print(n.val)
            dfs(n.right)

        self.res = None
        self.cntr = k
        dfs()
        return self.res

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
