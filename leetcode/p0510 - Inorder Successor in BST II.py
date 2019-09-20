"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        desc = node.right
        while desc and desc.left:
            desc = desc.left
        ansc = node.parent if not desc else None
        while ansc and ansc.right == node:
            ansc, node = ansc.parent, ansc
        return desc or ansc
