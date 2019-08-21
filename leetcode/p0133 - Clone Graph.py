# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraphDFS(self, node):
        graphCopy = {}
        def dfsCopy(node):
            if not node:
                return None
            nodeCopy = UndirectedGraphNode(node.label)
            graphCopy[node.label] = nodeCopy
            for neighbor in node.neighbors:
                if neighbor.label not in graphCopy:
                    dfsCopy(neighbor)
                nodeCopy.neighbors.append(graphCopy[neighbor.label])
            return nodeCopy

        return dfsCopy(node)

    def cloneGraph(self, node): # BFS
        if not node:
            return None
        d = {node.label : UndirectedGraphNode(node.label)}
        q = collections.deque([node])
        while q:
            cur = q.popleft()
            for nxt in cur.neighbors:
                if nxt.label not in d:
                    nxtCopy = UndirectedGraphNode(nxt.label)
                    d[nxt.label] = UndirectedGraphNode(nxt.label)
                    q.append(nxt)
                d[cur.label].neighbors.append(d[nxt.label])
        return d[node.label]
