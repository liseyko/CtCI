# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def _postorderTraversal(self, root: TreeNode):
        if root:
            self._postorderTraversal(root.left)
            self._postorderTraversal(root.right)
            self.res.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self._postorderTraversal(root)
        return self.res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stk, res = [root], []
        while any(stk):
            curNode = stk.pop()
            res.append(curNode.val)
            if curNode.left:
                stk.append(curNode.left)
            if curNode.right:
                stk.append(curNode.right)
        return res[::-1]
