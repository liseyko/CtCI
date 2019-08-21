# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.trees = {0: [], 1: [TreeNode(1)]}

    def shiftTree(self, t, k):
        if not t:
            return t
        res = TreeNode(t.val+k)
        res.left = self.shiftTree(t.left, k)
        res.right = self.shiftTree(t.right, k)
        return res

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n in self.trees:
            return self.trees[n]

        result = []
        for i in range(1, n+1):
            for leftSubTree in self.generateTrees(i-1) or [None]:
                for rightSubTree in self.generateTrees(n-i) or [None]:
                    r = TreeNode(i)
                    r.left = leftSubTree
                    r.right = self.shiftTree(rightSubTree, i)
                    result.append(r)
        self.trees[n] = result
        return result
