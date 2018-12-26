# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def getleaf(q):
            while q:
                node = q.pop()
                if not node.left and not node.right:
                    yield node.val
                else:
                    q.extend([c for c in (node.right, node.left) if c])

        for l1, l2 in itertools.zip_longest(getleaf([root1]), getleaf([root2])):
            if l1 != l2:
                return False
        return True
