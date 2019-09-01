class Solution:
    """ Serialize PreorderTraversal2Str then substr search """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def convert(p):
            return "^" + str(p.val) + "$" +\
             convert(p.left) +\
             convert(p.right) if p else "#"

        return convert(t) in convert(s)


class Solution:
    """ second: tree2list, then find sublist by bruteforce anyway"""
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        ss, ts = [], []

        def dfs(n, st):
            if not n:
                st.append(None)
                return
            st.append(n.val)
            dfs(n.left, st)
            dfs(n.right, st)

        dfs(s, ss)
        dfs(t, ts)
        for i in range(len(ss) - len(ts)+1):
            if ts == ss[i:i+len(ts)]:
                return True
        return False


class Solution:
    """ first bruteforce solution """
    def _isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if getattr(s, 'val', None) != getattr(t, 'val', None):
            return False
        return s == t or\
            self._isSameTree(s.left, t.left) and\
            self._isSameTree(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self._isSameTree(s, t) or s and\
            (self.isSubtree(s.left, t) or
             self.isSubtree(s.right, t))
