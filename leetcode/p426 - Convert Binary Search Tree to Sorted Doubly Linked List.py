"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    # left pointer = predecessor
    # right pointer = successor
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        q = []

        def dfs(n=root):
            if n.right:
                dfs(n.right)
            q.append(n)
            if n.left:
                dfs(n.left)

        if not root:
            return None

        dfs()
        res = q[-1]
        q[-1].left, q[0].right = q[0], q[-1]
        while q:
            cur = q.pop()
            if q:
                cur.right, q[-1].left = q[-1], cur

        return res
