# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:

        def dfs(node):
            if not node:
                return
            self.buf.append(node)
            if not node.left and not node.right:
                if not self.res: # or len(self.res) >  len(self.buf):
                    self.res = self.buf[:]
                else: # if len(self.buf) == len(self.res):
                    i, j = len(self.buf)-1, len(self.res)-1
                    while self.buf[i] != self.res[j] and\
                          self.buf[i].val <= self.res[j].val:
                        if self.buf[i].val < self.res[j].val:
                            self.res = self.buf[:]
                            break
                        i, j = i-1, j-1
            dfs(node.left)
            dfs(node.right)
            self.buf.pop()

        self.res, self.buf = [], []
        dfs(root)
        return ''.join(chr(ord('a')+n.val) for n in self.res[::-1])
