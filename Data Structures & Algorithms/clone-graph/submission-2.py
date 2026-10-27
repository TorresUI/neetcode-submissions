"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        if not node:
            return None

        def dfs(node):
            if node not in oldToNew:
                newNode = Node(node.val)
                oldToNew[node] = newNode
            
            #If the node exists in the map iterate through the neightbors and append them to the nodes neighbor list
            copyNode = oldToNew[node]

            for i in node.neighbors:
                if i not in oldToNew:
                    newNeighbor = dfs(i)
                else:
                    newNeighbor = oldToNew[i]
                copyNode.neighbors.append(newNeighbor)
            return copyNode
        dfs(node)

        return oldToNew[node]
