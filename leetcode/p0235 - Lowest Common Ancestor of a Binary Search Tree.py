class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodes = [root]
        if q.val < p.val:
            p, q = q, p 
        while any(nodes):
            n = nodes.pop()
            if p.val <= n.val <= q.val:
                return n
            nodes.extend([c for c in (n.right, n.left) if c])
        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val < p.val:
            p, q = q, p
        n = root
        while n:
            if p.val <= n.val <= q.val:
                return n
            elif p.val > n.val:
                n = n.right
            else:
                n = n.left
        return None
