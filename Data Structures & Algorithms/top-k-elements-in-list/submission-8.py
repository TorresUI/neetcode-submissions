class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [[] for _ in range(len(nums))]
        freqMap = {}
        res = []
        for i in nums:
            freqMap[i] = 1 + freqMap.get(i, 0)
        
        for num in list(freqMap.keys()):
            freqList[freqMap[num] - 1].append(num)
        
        for n in reversed(freqList):
            while k > 0 and len(n) != 0:
                res.append(n.pop())
                k -= 1
        
        return res