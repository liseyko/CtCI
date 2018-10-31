# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        vis = {}

        def dfs(x):
            if not x: return None
            if x.label not in vis:
                r = UndirectedGraphNode(x.label)
                vis[x.label] = r
                for n in x.neighbors:
                    r.neighbors.append(dfs(n))
            return vis[x.label]

        return dfs(node)