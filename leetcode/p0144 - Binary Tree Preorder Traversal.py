# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] +\
            self.preorderTraversal(root.left) +\
            self.preorderTraversal(root.right)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stk = [root]
        result = []
        while any(stk):
            currentNode = stk.pop()
            result.append(currentNode.val)
            if currentNode.right:
                stk.append(currentNode.right)
            if currentNode.left:
                stk.append(currentNode.left)
        return result
