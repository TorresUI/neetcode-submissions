class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        while k < len(self.minHeap):
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        print(self.minHeap)
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        else:
            if val > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, val)
        
        return self.minHeap[0]
        
