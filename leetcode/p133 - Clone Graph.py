# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # TODO: BFS
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
