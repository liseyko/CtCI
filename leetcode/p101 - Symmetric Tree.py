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
