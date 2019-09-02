class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        """1st attempt"""
        def dfs(n=root):
            if not n:
                return
            if n.val not in seen:
                heapq.heappushpop(heap, -n.val)
                seen.add(n.val)
            dfs(n.left)
            dfs(n.right)
        heap = [float('-inf'), float('-inf')]
        seen = set()
        dfs()
        return -1 if float('-inf') in heap else -1*heap[0]

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        minVal = root.val if root else None
        nodes = collections.deque([root])
        res = float('inf')
        while any(nodes):
            n = nodes.popleft()
            if n.val > minVal:
                res = min(res, n.val)
            for c in (n.left, n.right):
                if c:
                    nodes.append(c)
        return -1 if res == float('inf') else res
