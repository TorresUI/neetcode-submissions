class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #Break this down to sub problems
        #The permutation of 1 , 2 , 3 is really just 1 in every spot of the permutation of 2, 3
        #The permutation of 2, 3 is really just 2 in every spot of the permutations of 3, 
        #The permutation of 3 is really just 3 in every spot of the permutation of []

        def dfsPerm(i):
            #Base case: we have reached the end of the list now we can start bubbling back up to the top. 
            if i >= len(nums):
                return [[]]
            

            currentPermutations = dfsPerm(i+1)
            newPerms = []
            for perm in currentPermutations:
                #[]
                for index in range(len(perm) + 1):
                    copyArray = perm.copy()
                    copyArray.insert(index, nums[i])
                    newPerms.append(copyArray)
            return newPerms
        
        return dfsPerm(0)