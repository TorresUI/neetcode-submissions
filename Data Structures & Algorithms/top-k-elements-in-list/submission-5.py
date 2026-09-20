class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)

        freqList = []
        for i in range(len(nums)):
            freqList.append([])
        for num in list(freqMap.keys()):
            freq = freqMap[num]
            freqList[freq - 1].append(num)
        
        res = []
        for l in reversed(freqList):
            while k > 0 and l:
                temp = l.pop()
                res.append(temp)
                k -= 1
        
        return res