class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #map : value -> freq
        # Highest freq is len(nums)
        freqMap = {}

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)
        
        freqArray = []
        for i in range(len(nums) + 1): 
            freqArray.append([])
        
        for i in freqMap.keys():
            freqArray[freqMap[i]].append(i) 

        res = []
        r = len(freqArray) - 1
        while r > 0 and k != 0:
            #iterate backwards and add to the result array elements and decrease k at each point
            #first check if the current index array is valid
            if not freqArray[r]:
                r -= 1
                continue
            
            #otherwise pop from the array and add to the result
            res.append(freqArray[r].pop())
            k -= 1
        return res