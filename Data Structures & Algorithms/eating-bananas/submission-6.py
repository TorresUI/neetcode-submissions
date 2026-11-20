class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #I know the max speed I can eat the piles is the max number in piles. This will guarentee that I can eat all the piles in len(piles) hours. so if h  < len(piles) this problem cannot be solved

        #find the minimum amount of bannanas we can eat the piles with we know we can eat from 1 - h so just do binary search and then iterate through the piles of bananas and see if we can eat them

        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:

            #Find the mid number this is also our eating rate (k)
            m = l + ((r - l) // 2)

            #see if we can finish the bannanas.
            hours = 0
            for p in piles:
                #round up division therefore if the res is less than 0 its 1 and if the res is 2.2 its 3 
                hours += (math.ceil(p / m))
            
            #Now we have how many hours its going to take to eat the piles at an eating rate of k
            if hours <= h:
                #we found a solution that eats faster than expected. decrease k and see if we can find a solution that uses a smaller k
                res = min(res, m)
                r = m - 1
            elif hours > h:
                #we need to eat with a greater k
                l = m + 1
        return res



