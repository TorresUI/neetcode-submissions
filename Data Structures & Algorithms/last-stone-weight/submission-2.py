class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for s in stones:
            minHeap.append(-s)
        
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            y = heapq.heappop(minHeap)
            x = heapq.heappop(minHeap)

            if abs(x) < abs(y):
                heapq.heappush(minHeap, -(abs(y) - abs(x)))
        
        return abs(minHeap[0]) if minHeap else 0