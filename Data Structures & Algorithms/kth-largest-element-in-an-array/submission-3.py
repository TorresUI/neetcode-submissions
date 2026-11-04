class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for n in range(len(nums)):
            nums[n] = -nums[n]
        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1
        return -nums[0]