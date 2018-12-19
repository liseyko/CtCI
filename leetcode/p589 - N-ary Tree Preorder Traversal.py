"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """ Recursive Solution
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        r = [root.val]
        
        for c in root.children:
            if c:
                r.extend(self.preorder(c))
        return r

    def preorder(self, root):
        """ Iterative Solution
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        q = [root]
        r = []
        
        while q:
            node = q.pop()
            r.append(node.val)
            for c in node.children[::-1]:
                if c:
                    q.append(c)
        return r