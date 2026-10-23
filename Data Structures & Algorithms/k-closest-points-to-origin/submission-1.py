class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for p in points:
            x, y = p
            eDistance = (x ** 2) + (y ** 2)
            minHeap.append([eDistance, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            output = heapq.heappop(minHeap)
            res.append([output[1], output[2]])
            k -= 1
        return res