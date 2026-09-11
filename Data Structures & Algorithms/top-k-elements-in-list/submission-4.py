class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [[] for _ in range(len(nums) + 1)]
        freqMap = {} #maps the key(the number in nums) to the val (how freq it is)
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        
         
        for num, count in freqMap.items():
            freqList[count].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            while freqList[i] and len(res) != k:
                res.append(freqList[i].pop())

        
        return res