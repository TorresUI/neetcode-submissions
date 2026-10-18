class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for i in stones:
            minHeap.append(-i)
        
        heapq.heapify(minHeap)
        
        while len(minHeap) > 1:
            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)

            if x < y:
                result = abs(x) - abs(y)
                heapq.heappush(minHeap, -result)
        
        return abs(minHeap[0]) if minHeap else 0
