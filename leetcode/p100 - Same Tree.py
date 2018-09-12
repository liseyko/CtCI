from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q): 
        """ # [ via BFS ] #
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        p_queue, q_queue = deque([p]), deque([q])

        while p_queue and q_queue:
            pn, qn = p_queue.popleft(), q_queue.popleft()
            if pn and qn and pn.val == qn.val:
                p_queue.append(pn.left)
                p_queue.append(pn.right)
                q_queue.append(qn.left)
                q_queue.append(qn.right)
            elif pn is None and qn is None:
                pass
            else:
                return False
        if p_queue or q_queue:
                return False
        return True
