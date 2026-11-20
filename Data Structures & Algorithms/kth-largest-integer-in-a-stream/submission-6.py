class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #kth largest is also the smallest out of a list of k
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        #Lets make sure minHeap is of size k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        #now we have a minHeap of size k so the element at the top should be the smallest out of size k otherwise known as the kth largest element.

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        #adding the integer to the minHeap. If this int is larger it can influence the size of the kth largest and if its smaller it can influence the kth largest if our minheap is not yet at size k if it is exceeding k this will just get popped
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
        
