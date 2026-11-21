class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #union find. 
        #create edges across all points in the graph then start at point 0 and start storing its neighbors in a minHeap and popping the shortest path. then additing its neighbors to the heap and repeat until all nodes are visited. then return the distance

        adjList = defaultdict(list)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]

                manDistance = abs(xi - xj) + abs(yi - yj)

                #append man distance as weighted edge to both vertices.
                adjList[i].append([manDistance, j])
                adjList[j].append([manDistance, i])

        #now that we have the adjList we can add 0's points to the minheap
        minHeap = adjList[0].copy()
        heapq.heapify(minHeap)
        visited = set()
        visited.add(0)
        distance = 0
        
        while len(visited) != len(points):
            #pop from the heap.
            dis, p = heapq.heappop(minHeap)
            #Now we are at a new point. Add the distance to the total distance
            #mark it as visited.
            #add its neighbors into the minHeap
            if p in visited:
                continue
            distance += dis
            visited.add(p)


            #Now process its neighbors
            neighbors = adjList[p]
            for n in neighbors:
                heapq.heappush(minHeap, n)
        return distance


