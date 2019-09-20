# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        root = curNode = TreeNode("")
        stk = [curNode]

        for i, c in enumerate(s):
            if c == '(':
                if s[i-1] != ')':
                    stk.append(curNode)
                curNode  = TreeNode("")
                if s[i-1] != ')':
                    stk[-1].left = curNode
                else:
                    stk[-1].right = curNode
            elif c == ')':
                if s[i-1] == ')':
                    stk.pop()
            else:
                curNode.val += c

        return root if s else None
