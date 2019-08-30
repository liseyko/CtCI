class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return 1+max([0]+[self.maxDepth(c) for c in root.children])

    def maxDepth(self, root: 'Node') -> int:
        stack = [(1, root)] if root else None
        maxdepth = 0

        while stack:
            depth, node = stack.pop()
            if node:
                maxdepth = max(maxdepth, depth)
                for c in node.children:
                    stack.append((depth + 1, c))

        return maxdepth
