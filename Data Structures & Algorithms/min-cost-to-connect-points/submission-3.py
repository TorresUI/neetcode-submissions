class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                
                #otherwise
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                adjList[i].append([dist, j])
                adjList[j].append([dist, i])
        
        minHeap = [[0, 0]]
        visit = set()
        minCost = 0

        while minHeap and len(visit) < len(points):
            dist, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            
            #otherwise point is a new point
            minCost += dist
            visit.add(point)

            #check neighbors of this new point
            for d2, p2 in adjList[point]:
                heapq.heappush(minHeap, [d2, p2])
        
        return minCost

