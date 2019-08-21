"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return []
        
        q, r, ql = collections.deque([root]), [[]], 1
        
        while ql or q:
            n = q.popleft()
            ql -= 1
            r[-1].append(n.val)
            for c in n.children:
                if c:
                    q.append(c)
            if not ql and q:
                ql = len(q)
                r.append([])
                
        return r
    
    def levelOrder(self, root):
        q, ret = [root], []
        if root:
            while q:
                ret.append([node.val for node in q])
                q = [child for node in q for child in node.children if child]
        return ret