class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, t in times:
            adjList[u].append([t, v])
        
        visited = set()
        minHeap = [[0, k]]
        totalTime = 0
        while minHeap and len(visited) < n:
            cost, currNode = heapq.heappop(minHeap)

            if currNode in visited:
                #Dont want to revisit already visited nodes
                continue
            
            #process newest node
            visited.add(currNode)
            totalTime = cost
            neighbors = adjList[currNode]

            for t2, n2 in neighbors:
                heapq.heappush(minHeap, [totalTime + t2, n2])
        
        return totalTime if len(visited) == n else -1
