class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k

        while len(self.minHeap) > k:
            #pop elements from the heap
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]