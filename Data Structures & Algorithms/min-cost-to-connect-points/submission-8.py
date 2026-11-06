class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in range(len(points)):
            for p in range(len(points)):
                    if i != p:
                        x1, y1 = points[i]
                        x2, y2 = points[p]
                        manDistance = abs(x1 - x2) + abs(y1 - y2)
                        adjList[i].append([manDistance, p])
            
            #Now we have a connected graph with edges to all nodes and weights assigned to those edges. We now need to find the minimum cost path so we will use Primms algorithm
        visited = set()
        minHeap = [[0, 0]]
        totalCost = 0

        while minHeap and len(visited) < len(points):
            cost, currPoint = heapq.heappop(minHeap)
            if currPoint in visited:
                #ignore already visited nodes. We do not want cycles
                continue
            
            #We have a point that has not been visited yet and has the lowest cost
            totalCost += cost
            visited.add(currPoint)

            #Now we need to process the current points neighbors
            neighbors = adjList[currPoint]
            
            for c2, p2 in neighbors:
                heapq.heappush(minHeap, [c2, p2])
        return totalCost

