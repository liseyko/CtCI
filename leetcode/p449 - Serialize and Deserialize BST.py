import bisect

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        data = []

        def dfs(n):
            if n:
                data.append(unichr(n.val))
                dfs(n.left)
                dfs(n.right)
        dfs(root)
        return u''.join(data)

    def _deserialize(self, data):
        root = TreeNode(data[0]) if data else None
        if len(data) > 1:
            mid = bisect.bisect_left(data, data[0], 1)
            root.left = self._deserialize(data[1:mid])
            root.right = self._deserialize(data[mid:])
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        return self._deserialize(map(ord, data))


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def dfs(n):
            if n:
                data.append(unichr(n.val))
                dfs(n.left)
                dfs(n.right)
        data = []
        dfs(root)
        return u''.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def _deserialize(s, e):
            root = TreeNode(data[s]) if e-s > 0 else None
            if e-s > 1:
                mid = bisect.bisect_left(data, data[s], s+1, e)
                root.left = _deserialize(s+1, mid)
                root.right = _deserialize(mid, e)
            return root

        data = map(ord, data)
        return _deserialize(0, len(data))
