class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #The problem is asking us to return false if there is a way to have two subsets with equal sums.
        #If you have two subsets with equal sums that adds up to the total sum then each subset needs to add up to totalsum/2
        #This number will be our target number. then we need to find if there is any combination to form this target number and we can safely assume the remainder can form target number and thus return true. 
        #For each number in the array we have two decisions we can either include it or exclude it we need to track all possible scenarios for all the numbers and then return if we ever see the target number
        targetSum = sum(nums) / 2
        combinations = set()
        combinations.add(0)

        for i in nums:
            #We need to have the set contain all options of wether we add the current number or not
            tempSet = combinations.copy()
            for c in combinations:
                tempSet.add(i + c)
                if i + c == targetSum:
                    return True
            combinations = tempSet
        return False

# 0 
# 0, 1
# 0, 3, 2, 
# 0, 3, 2, 6, 5, <--- found the target number 5 return
