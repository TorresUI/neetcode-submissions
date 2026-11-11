class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd, maxProd = 1, 1
        #res = max number just incase we get something like [0, 5, 0] where the max element is the result
        res = max(nums)

        for num in nums:
            if num == 0:
                #reset to 1 and continue
                minProd, maxProd = 1, 1
                continue
            
            #No 0 value so we can just multiply as usual
            newMinProd = minProd * num
            newMaxProd = maxProd * num

            minProd = min(newMinProd, newMaxProd, num)
            maxProd = max(newMinProd, newMaxProd, num)

            res = max(res, maxProd)
        
        return res
        