class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}

        for i in range(n):
            adjList[i] = []
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        #Need a visited set
        visit = set()

        def dfs(currentNode, prev):
            if currentNode in visit:
                return
            
            #process currentNode
            visit.add(currentNode)
            neighbors = adjList[currentNode]

            for i in neighbors:
                if i != prev:
                    dfs(i, currentNode)
            return
        
        #DFS just adds all connected nodes to the visit set.

        #iterate through all possible nodes check if they are not in visit if they are not it is a new graph.
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i, None)
                res += 1
        
        return res