class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            #We want to run this k + 1 levels in order to stop k times. beyond that is not possible

            #create temp array that is a copy of our prices
            temp = prices.copy()
            for s, d, p in flights:
                #s = source, d = destination, p = price
                #What is the cost to get to source?
                sCost = prices[s]
                if sCost + p < temp[d]:
                    #then we want to update this value in our temp array
                    temp[d] = sCost + p
                else:
                    continue
            prices = temp
        return prices[dst] if prices[dst] != float("inf") else -1