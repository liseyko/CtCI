# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.path = []
        while root:
            self.path.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.path:
            return True
        
    def next(self):
        """
        :rtype: int
        """
        if not self.path:
            return None
        cur = self.path.pop()
        nxt = cur.right
        while nxt:
            self.path.append(nxt)
            nxt = nxt.left
        return cur.val
