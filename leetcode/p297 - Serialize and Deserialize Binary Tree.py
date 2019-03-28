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
        result = []
        nodes = collections.deque([root]) if root else None
        while nodes:
            node = nodes.popleft()
            result.append(getattr(node, 'val', 'null'))
            if node:
                for child in (node.left, node.right):
                    nodes.append(child)

        while result and not result[-1]:
            result.pop()

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        node = root = TreeNode(data[0]) if data else None
        nodes = collections.deque([node]) if node else None
        i = 1
        while nodes and i < len(data):
            node = nodes.popleft()
            for child in ('left', 'right'):
                if i < len(data):
                    setattr(node, child, TreeNode(data[i]))
                    nodes.append(getattr(node, child))
                    i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
