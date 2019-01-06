# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        q = collections.deque([root])
        while any(q):
            qlen = len(q)
            while qlen:
                node = q.popleft()
                qlen -= 1
                if qlen:
                    node.next = q[0]
                for c in [node.left, node.right]:
                    if c:
                        q.append(c)
