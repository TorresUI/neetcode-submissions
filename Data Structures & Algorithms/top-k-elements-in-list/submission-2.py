class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [[] for _ in range(len(nums) + 1)]
        freqMap = {} #maps the key(the number in nums) to the val (how freq it is)
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
        
        freqMapKeys = list(freqMap.keys()) 
        for num in freqMapKeys:
            freqList[freqMap[num]].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            while freqList[i] and len(res) != k:
                res.append(freqList[i].pop())

        
        return res