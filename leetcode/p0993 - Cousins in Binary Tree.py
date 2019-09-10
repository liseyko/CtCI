class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        lvl = [root]
        while any(lvl):
            cur_lvl, lvl, nv2p = lvl, [], {}
            for node in cur_lvl:
                for chld in (node.left, node.right):
                    if chld:
                        lvl.append(chld)
                        nv2p[chld.val] = node
            if x in nv2p and y in nv2p:
                return nv2p[x] != nv2p[y]
        return False
