# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def _inorderTraversal(self, root):
        if not root:
            return []
        self._inorderTraversal(root.left)
        self.res.append(root.val)
        self._inorderTraversal(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self._inorderTraversal(root)
        return self.res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = \
            self.inorderTraversal(root.left) +\
            [root.val] +\
            self.inorderTraversal(root.right)
        return result

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stk, curr = [], [], root
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            res.append(curr.val)
            curr = curr.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """ TODO: Morris Traversal """
        pass
