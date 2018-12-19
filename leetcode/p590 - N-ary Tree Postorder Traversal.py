"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        r = []
        if not root:
            return r
        for c in root.children:
            if c:
                r.extend(self.postorder(c))
        
        return r + [root.val]
    
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        if not root: return []
        r, q = [], [root]
        
        while q:
            node = q.pop()
            r.append(node.val)
            for c in node.children:
                if c:
                    q.append(c)
        return r[::-1]