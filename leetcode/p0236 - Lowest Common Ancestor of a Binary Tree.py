class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca_idx, found1 = 0, False
        treeNodeChldNameList = ['right', 'left']
        stack = [(root, treeNodeChldNameList[:])] if root else None
        while stack:
            node, unprocChldrn = stack[-1]
            if len(unprocChldrn) == 2 and (node == p or node == q):
                if found1:
                    return stack[lca_idx][0]
                found1 = True
                lca_idx = len(stack)-1

            if unprocChldrn:
                nxtNode = getattr(node, unprocChldrn.pop())
                if nxtNode:
                    stack.append((nxtNode, treeNodeChldNameList[:]))
            else:
                del stack[-1]
                lca_idx = min(lca_idx, len(stack)-1)


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        lca = None
        stk = [(root, [root.right, root.left])]
        while stk:
            if len(stk[-1][1]) == 2:  # first encounter
                r = stk[-1][0]
                if r == p or r == q:
                    if lca is not None:
                        return stk[lca][0]
                    else:
                        lca = len(stk)-1
            if stk[-1][1]:
                c = stk[-1][1].pop()
                if c:
                    stk.append((c, [c.right, c.left]))
            else:
                stk.pop()
                if lca == len(stk):
                    lca -= 1

    def lowestCommonAncestor(self, root, p, q):
        stk, lca = [[root, 2]], -1
        while stk:
            n, paths = stk[-1]
            if paths:
                if paths == 2:  # first encounter
                    if n == p or n == q:
                        if lca >= 0:
                            return stk[lca][0]
                        else:
                            lca = len(stk)-1
                    c = n.left
                elif paths == 1:  # second
                    c = n.right
                stk[-1][1] -= 1
                if c:
                    stk.append([c, 2])
            else:  # final
                stk.pop()
                if lca == len(stk):
                    lca -= 1

    def lowestCommonAncestor(self, root, n1, n2):
        # states:
        # Unprocesed, Left/Right proccesed
        U, L, R = 2, 1, 0
        found = False
        lca_idx = -1
        stk = [[root, U]]
        while stk:
            cn, state = stk[-1]
            if state == U:
                if cn == n1 or cn == n2:
                    if not found:
                        found = True
                        lca_idx = len(stk)-1
                    else:  # found both
                        return stk[lca_idx][0]
                stk[-1][1] -= 1
                if cn.left:
                    stk.append([cn.left, U])
            elif state == L:
                stk[-1][1] -= 1
                if cn.right:
                    stk.append([cn.right, U])
            else:
                stk.pop()
                if found and lca_idx == len(stk):
                    lca_idx -= 1


UNPROC, LEFT, BOTH = 0, 1, 2


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [[root, UNPROC]] if root else None
        found, result = False, None
        lookup = {p, q}
        while stack:
            node, status = stack[-1]

            if node in lookup:
                lookup.remove(node)
                if found:
                    return result
                else:
                    found, result = True, node

            if status == UNPROC:
                stack[-1][1] = LEFT
                if node.left:
                    stack.append([node.left, UNPROC])
            elif status == LEFT:
                stack[-1][1] = BOTH
                if node.right:
                    stack.append([node.right, UNPROC])
            elif status == BOTH:
                stack.pop()
                if found and result == node:
                    result = stack[-1][0] if stack else None
