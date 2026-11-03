class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, t in times:
            edges[u].append([t, v])
        
        #k is the starting node
        minHeap = []
        for i in edges[k]:
            minHeap.append(i)
        heapq.heapify(minHeap)
        visited = set()
        visited.add(k)
        time = 0
        while minHeap:
            cost, targetNode = heapq.heappop(minHeap)
            if targetNode in visited:
                continue
            time = cost
            visited.add(targetNode)
            neighbors = edges[targetNode]
            for c, t in neighbors:
                heapq.heappush(minHeap, [c + cost, t])
        
        return time if len(visited) == n else -1

