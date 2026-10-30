class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}

        for i in range(n):
            adjList[i] = []

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        #run dfs from node 0
        visited = set()

        def dfs(currentNode, prev):
            if currentNode in visited:
                return False
            
            #otherwise process the node and its neighbors
            visited.add(currentNode)
            neighbors = adjList[currentNode]

            for node in neighbors:
                print(node, currentNode)
                if node != prev:
                    if dfs(node, currentNode) == False:
                        return False
            return True
        res = dfs(0, None)
        return True if res and len(visited) == n else False