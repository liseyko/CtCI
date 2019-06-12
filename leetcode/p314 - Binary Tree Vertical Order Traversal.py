# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTreeDepth(self, root):
        return 1 + max(self.getTreeDepth(root.left),
                       self.getTreeDepth(root.right)) if root else 0

    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        res = [[] for _ in range(2*self.getTreeDepth(root))]
        lvl = [(root, len(res)//2)] if root else None
        while lvl:
            nxtLvl = []
            for node, nodeIdx in lvl:
                res[nodeIdx].append(node.val)
                if node.left:
                    nxtLvl.append((node.left, nodeIdx-1))
                if node.right:
                    nxtLvl.append((node.right, nodeIdx+1))
            lvl = nxtLvl

        return [lst for lst in res if lst]
