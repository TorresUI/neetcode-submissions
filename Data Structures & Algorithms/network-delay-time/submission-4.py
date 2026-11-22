class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #make an adj list map so that we can have fast look up times for edges

        adjList = defaultdict(list)

        for u, v, t in times:
            adjList[u].append([t, v])
        
        minHeap = adjList[k]
        heapq.heapify(minHeap)
        minutes = 0
        visited = set()
        visited.add(k)

        #pop one element from the minHeap every time. add the current distance 
        while minHeap and len(visited) != n:
            #pop from minHeap
            time, point = heapq.heappop(minHeap)
            minutes = time

            if point in visited:
                continue
            
            #we are at a new point. proccess it then add its neighbors to the minHeap
            visited.add(point)
            for t2, p2 in adjList[point]:
                heapq.heappush(minHeap, [t2 + time, p2])
        
        return minutes if len(visited) == n else -1