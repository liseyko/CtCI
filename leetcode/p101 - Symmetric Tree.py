from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root):
        """ [via BFS again]
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left and root.right and root.left.val != root.right.val:
            return False

        l_queue, r_queue = deque([root.left]), deque([root.right])

        while l_queue and r_queue:
            ln, rn = l_queue.popleft(), r_queue.popleft()
            if ln and rn and ln.val == rn.val:
                l_queue.append(ln.left)
                r_queue.append(rn.right)
                l_queue.append(ln.right)
                r_queue.append(rn.left)
            elif ln is None and rn is None:
                pass
            else:
                return False
        if l_queue or r_queue:
                return False
        return True

    def isSymmetric(self, root):
        level = [root]
        while any(level):
            level = [c for n in level if n for c in (n.left, n.right)]
            for i in range(len(level) // 2):
                if getattr(level[i], 'val', None) != \
                   getattr(level[~i], 'val', None):
                    return False
        return True

    def isSymmetric(self, root):
        def isMirror(root1, root2):
            if not root1 and not root2:
                return True
            elif not (root1 and root2):
                return False
            return root1.val == root2.val and \
                isMirror(root1.left, root2.right) and \
                isMirror(root2.left, root1.right)

        return isMirror(root, root)
