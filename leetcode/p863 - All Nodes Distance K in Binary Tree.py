# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        res = []

        def distance(root, k, children=["left", "right"]):
            if not root:
                return
            if k == 0:
                res.append(root.val)
            else:
                children = [getattr(root, c) for c in children]
                for c in children:
                    distance(c, k-1)

        def findTarget(n=root, path=[]):
            tgtPath = (None, None)
            if not n:
                return tgtPath
            if n == target:
                return n, path
            if n.left:
                tgtPath = findTarget(n.left, path+[(n, "right")])
            if n.right and not tgtPath[0]:
                tgtPath = findTarget(n.right, path+[(n, "left")])
            return tgtPath

        n, path = findTarget()
        distance(n, k)
        while k and path:
            k -= 1
            parent, child = path.pop()
            distance(parent, k, [child])

        return res
