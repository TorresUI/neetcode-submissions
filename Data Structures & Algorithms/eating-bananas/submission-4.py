class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #to calculate divide each pile by k and and round up sum all the results and that is h
        #as long as h is <= 9 that is a valid k
        maxNumInPile = max(piles)
        
        l, r = 1, maxNumInPile
        res = maxNumInPile
        while l <= r:
            m = l + ((r - l) // 2)
            #We have our k value (validkRange[m])
            #we need to compute the h
            currentHours = 0
            for p in piles:
                currentHours += math.ceil(p / m)
            #we have the k and h we want to check if currentHours is less than or equal to h if it is then take the min res

            if currentHours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res

        
