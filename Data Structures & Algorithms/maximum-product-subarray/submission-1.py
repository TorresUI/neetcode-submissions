class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        prevMin, prevMax = 1, 1

        for i in nums:
            if i == 0:
                prevMin, prevMax = 1, 1
                continue
            #If i is a negative number prevMinProduct will become the new max number since the negative will flip prevMin(negative) into a positive
            prevMinProduct = i * prevMin
            #Max product holds the max product for all given subarrays that end at index i 
            prevMaxProduct = i * prevMax
            
            #set the new min and max
            #use the minProduct/maxProduct and n 
            #n if we want to restart the subarray and found a new highest number
            #min to track incase we run into a negative that can flip the sign
            #max to track for positive values to keep increasing
            prevMin = min(i, prevMinProduct, prevMaxProduct)
            prevMax = max(i, prevMaxProduct, prevMinProduct)
            #Save any new max solutions
            res = max(res, prevMax)
        
        return res